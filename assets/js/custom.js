$(document).ready(function() {

    (function(kh, $, undefined) {

        // Public variables
        kh.selected = [];      // list of selected facets
        kh.containedBy = {};   // maps {facet: count} to containers
        kh.containers = {};
        kh.sortBy = {};
        kh.iframes = {};
        $rows = $("table").find("tr:has(td)");
        $facets = $("ul.faceted").find("li");
        $sortButtons = $("img.sortFacet");
        const pageName = window.location.pathname;

        // Public methods
        kh.toggleSubmenu = function(e) {
            var $this = $(this);
            $this.off("click");
            e.preventDefault();
            $this.parent("a").next("ul").toggleClass("hidden");
            $this.on("click", kh.toggleSubmenu);
        }

        kh.changeFacetSort = function() {
            let $im = $(this);
            let parentID = $im.parents("nav").find("ul").attr("id");
            ["alpha", "count"].forEach(function (sortCrit) {
                if ($im.hasClass(sortCrit) & kh.sortBy[parentID] != sortCrit) {
                    let $buttons = $im.parents("nav").find("img");
                    $buttons.removeClass("selected");
                    $buttons.filter("." + sortCrit).addClass("selected");
                    kh.sortBy[parentID] = sortCrit;
                    kh.updateFacets();
                    return;
                }
            });
        }

        kh.toggleFacet = function(e) {
            var $this = $(this);
            $this.off("click");
            e.preventDefault();
            kh.toggleFacetFromText($this.text());
            kh.pushState();
            $this.off("click").on("click", kh.toggleFacet);
        }

        kh.toggleFacetFromText = function(tag) {
            if (kh.selected.includes(tag)) {
                kh.selected.splice(kh.selected.indexOf(tag), 1);
            } else { kh.selected.push(tag); }
            $rows.removeClass("hidden");
            if (kh.selected.length !== 0) {
                $rows.each(function() { 
                    var $row = $(this);
                    var tags = $row.data("tags").split("|");
                    if (!(tags.filter(x => kh.selected.includes(x)).length == kh.selected.length)) {
                        $row.addClass("hidden");
                    }
                });
            }
            kh.updateFacets();
        }

        kh.toggleFacetsFromURL = function() {
            const params = new URLSearchParams(window.location.search);
            const topics = params.getAll("topic");
            kh.selected = [];
            if (topics.length !== 0) {
                topics.forEach(function(val) {
                    kh.toggleFacetFromText(val.replaceAll("-", " "));
                });
            } else { $rows.removeClass("hidden"); kh.updateFacets(); }
        }

        kh.updateFacets = function() {

            // Initialize facet containers
            if ($.isEmptyObject(kh.containers)) {
                $facets.each(function() {
                    let facet = $(this).text();
                    let parentID = $(this).parent("ul").attr("id");
                    if (parentID in kh.containers) {
                        kh.containers[parentID][facet] = 0;
                    } else { kh.containers[parentID] = { facet: 0 }; }
                    kh.containedBy[facet] = $(this).parent("ul");
                    kh.sortBy[parentID] = "count";
                });
            } else {
                for (parentID in kh.containers) {
                    let $parent = $("#" + parentID);
                    for (facet in kh.containers[parentID]) {
                        kh.containers[parentID][facet] = 0;
                        kh.containedBy[facet] = $parent;
                    }
                }
            }

            // Count active tags
            $rows.each(function() { 
                var $row = $(this);
                if (!$row.hasClass("hidden")) {
                    $row.data("tags").split("|").forEach(function(val) {
                        if (val.length !== 0) {
                            kh.containers[kh.containedBy[val].attr("id")][val] += 1;
                        }
                    })
                }
            });

            // Update facets in sidebar
            $facets.remove();
            for (parentID in kh.containers) {
                let facets = kh.containers[parentID];
                let sorted = (kh.sortBy[parentID] == "count")
                    ? Object.entries(facets).sort(
                        function(a, b) { return ((a[1] > b[1]) ? -1 : ((a[1] < b[1]) ? 1 : 0));
                    })
                    : Object.entries(Object.keys(facets).sort().reduce(
                        (obj, key) => { 
                        obj[key] = facets[key]; 
                        return obj;
                        }, {} ));
                
                sorted.forEach(function(val) {
                    if (val[0].length > 0 && val[1] > 0) {
                        var li = document.createElement("li");
                        var a = document.createElement("a");
                        a.href = pageName + "?topic=" + val[0].replaceAll(" ", "-")
                        a.innerText = val[0];
                        if (kh.selected.includes(val[0])) { a.classList.add("selected"); }
                        li.appendChild(a);
                        li.innerHTML += " (" + val[1] + ")";
                        kh.containedBy[val[0]].append(li);
                    }
                });
            }

            // Add handler
            $facets = $("ul.faceted").find("li");
            $facets.find("a").on("click", kh.toggleFacet);

            // Show reset button if any facets selected
            console.log(kh.selected)
            if (kh.selected.length) {
                $("#reset").show();
            } else { $("#reset").hide(); }
        }

        kh.pushState = function() {
            var href = window.location.href.split("?")[0];
            if (kh.selected.length) {
                href += "?"
                kh.selected.sort().forEach(function(val) {
                    href += "topic=" + val.replaceAll(" ", "-") + "&";
                });
                href = href.replace(/&$/, "");
            }
            if (href != window.location.href) {
                window.history.pushState( {} , "", href );
            }
        }

        kh.resetFilters = function() {
            window.history.pushState( {} , "", window.location.href.split("?")[0]);
            kh.toggleFacetsFromURL();
        }

        kh.resizeIframe = function() {
            $("iframe").each(function(e) {
                var $this = $(this);
                var key = $(this).attr("src");
                if (!(key in kh.iframes)) {
                    kh.iframes[key] = $this.width() / $this.height();
                }              
                var aspectRatio = kh.iframes[key];
                $this.attr("width", "100%");
                $this.attr("height", $(this).width() / aspectRatio);
            })
        }

        // Enable handlers
        // $("ul.collapsible li:has(ul) span.nav__sub-title").on("click", kh.toggleSubmenu);
        $("ul.faceted a").on("click", kh.toggleFacet);
        $("table.faceted tr td:nth-child(2) a").on("click", kh.toggleFacet);
        $("#reset").on("click", kh.resetFilters);
        $sortButtons.on("click", kh.changeFacetSort);
        $(window).on("resize", kh.resizeIframe);
        window.onpopstate = (event) => kh.toggleFacetsFromURL();

    }( window.kh = window.kh || {}, jQuery ));

    kh.resizeIframe();
    kh.updateFacets();
    kh.toggleFacetsFromURL();

});