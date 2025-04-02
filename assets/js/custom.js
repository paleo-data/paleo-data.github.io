$(document).ready(function() {

    (function(pkh, $, undefined) {

        // Public variables
        pkh.selected = [];      // list of selected facets
        pkh.containedBy = {};   // maps {facet: count} to containers
        pkh.containers = {};
        pkh.sortBy = {};
        pkh.iframes = {};
        $rows = $("table").find("tr:has(td)");
        $facets = $("ul.faceted").find("li");
        $sortButtons = $("img.sortFacet");
        const pageName = window.location.pathname;

        // Public methods
        pkh.toggleSubmenu = function(e) {
            var $this = $(this);
            $this.off("click");
            e.preventDefault();
            $this.parent("a").next("ul").toggleClass("hidden");
            $this.on("click", pkh.toggleSubmenu);
        }

        pkh.changeFacetSort = function() {
            let $im = $(this);
            let parentID = $im.parents("nav").find("ul").attr("id");
            ["alpha", "count"].forEach(function (sortCrit) {
                if ($im.hasClass(sortCrit) & pkh.sortBy[parentID] != sortCrit) {
                    let $buttons = $im.parents("nav").find("img");
                    $buttons.removeClass("selected");
                    $buttons.filter("." + sortCrit).addClass("selected");
                    pkh.sortBy[parentID] = sortCrit;
                    pkh.updateFacets();
                    return;
                }
            });
        }

        pkh.toggleFacet = function(e) {
            var $this = $(this);
            $this.off("click");
            e.preventDefault();
            pkh.toggleFacetFromText($this.text());
            pkh.pushState();
            $this.off("click").on("click", pkh.toggleFacet);
        }

        pkh.toggleFacetFromText = function(tag) {
            if (pkh.selected.includes(tag)) {
                pkh.selected.splice(pkh.selected.indexOf(tag), 1);
            } else { pkh.selected.push(tag); }
            $rows.removeClass("hidden");
            if (pkh.selected.length !== 0) {
                $rows.each(function() { 
                    var $row = $(this);
                    var tags = $row.data("tags").split("|");
                    if (!(tags.filter(x => pkh.selected.includes(x)).length == pkh.selected.length)) {
                        $row.addClass("hidden");
                    }
                });
            }
            pkh.updateFacets();
        }

        pkh.toggleFacetsFromURL = function() {
            const params = new URLSearchParams(window.location.search);
            const topics = params.getAll("topic");
            pkh.selected = [];
            if (topics.length !== 0) {
                topics.forEach(function(val) {
                    pkh.toggleFacetFromText(val.replace("-", " "));
                });
            } else { $rows.removeClass("hidden"); pkh.updateFacets(); }
        }

        pkh.updateFacets = function() {

            // Initialize facet containers
            if ($.isEmptyObject(pkh.containers)) {
                $facets.each(function() {
                    let facet = $(this).text();
                    let parentID = $(this).parent("ul").attr("id");
                    if (parentID in pkh.containers) {
                        pkh.containers[parentID][facet] = 0;
                    } else { pkh.containers[parentID] = { facet: 0 }; }
                    pkh.containedBy[facet] = $(this).parent("ul");
                    pkh.sortBy[parentID] = "count";
                });
            } else {
                for (parentID in pkh.containers) {
                    let $parent = $("#" + parentID);
                    for (facet in pkh.containers[parentID]) {
                        pkh.containers[parentID][facet] = 0;
                        pkh.containedBy[facet] = $parent;
                    }
                }
            }

            // Count active tags
            $rows.each(function() { 
                var $row = $(this);
                if (!$row.hasClass("hidden")) {
                    $row.data("tags").split("|").forEach(function(val) {
                        if (val.length !== 0) {
                            pkh.containers[pkh.containedBy[val].attr("id")][val] += 1;
                        }
                    })
                }
            });

            // Update facets in sidebar
            $facets.remove();
            for (parentID in pkh.containers) {
                let facets = pkh.containers[parentID];
                let sorted = (pkh.sortBy[parentID] == "count")
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
                        if (pkh.selected.includes(val[0])) { a.classList.add("selected"); }
                        li.appendChild(a);
                        li.innerHTML += " (" + val[1] + ")";
                        pkh.containedBy[val[0]].append(li);
                    }
                });
            }

            // Add handler
            $facets = $("ul.faceted").find("li");
            $facets.find("a").on("click", pkh.toggleFacet);
        }

        pkh.pushState = function() {
            var href = window.location.href.split("?")[0];
            if (pkh.selected.length) {
                href += "?"
                pkh.selected.sort().forEach(function(val) {
                    href += "topic=" + val.replace(" ", "-") + "&";
                });
                href = href.replace(/&$/, "");
            }
            if (href != window.location.href) {
                window.history.pushState( {} , "", href );
            }
        }

        pkh.resizeIframe = function() {
            $("iframe").each(function(e) {
                var $this = $(this);
                var key = $(this).attr("src");
                if (!(key in pkh.iframes)) {
                    pkh.iframes[key] = $this.width() / $this.height();
                }              
                var aspectRatio = pkh.iframes[key];
                $this.attr("width", "100%");
                $this.attr("height", $(this).width() / aspectRatio);
            })
        }

        // Enable handlers
        // $("ul.collapsible li:has(ul) span.nav__sub-title").on("click", pkh.toggleSubmenu);
        $("ul.faceted a").on("click", pkh.toggleFacet);
        $("table.faceted tr td:nth-child(2) a").on("click", pkh.toggleFacet);
        $sortButtons.on("click", pkh.changeFacetSort);
        $(window).on("resize", pkh.resizeIframe);
        window.onpopstate = (event) => pkh.toggleFacetsFromURL();

    }( window.pkh = window.pkh || {}, jQuery ));

    pkh.resizeIframe();
    pkh.updateFacets();
    pkh.toggleFacetsFromURL();

});