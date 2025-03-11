$(document).ready(function() {

    (function(pdh, $, undefined) {

        // Public variables
        pdh.selected = [];
        pdh.iframes = {};
        pdh.facets = {};
        $rows = $("table").find("tr:has(td)");
        $facets = $("ul.faceted").find("li");

        // Public methods
        pdh.toggleSubmenu = function(e) {
            var $this = $(this);
            $this.off("click");
            e.preventDefault();
            $this.parent("a").next("ul").toggleClass("hidden");
            $this.on("click", pdh.toggleSubmenu);
        }

        pdh.toggleFacet = function(e) {
            var $this = $(this);
            $this.off("click");
            e.preventDefault();
            // Toggle selected
            if (pdh.selected.includes($this.text())) {
                pdh.selected.splice(pdh.selected.indexOf($this.text()), 1);
            } else { pdh.selected.push($this.text()); }
            $rows.removeClass("hidden");
            if (pdh.selected.length !== 0) {
                $rows.each(function() { 
                    var $row = $(this);
                    var tags = $row.data("tags").split("|");
                    if (!(tags.filter(x => pdh.selected.includes(x)).length == pdh.selected.length)) {
                        $row.addClass("hidden");
                    }
                });
            }
            pdh.updateFacets();
            $this.off("click").on("click", pdh.toggleFacet);
        }

        pdh.updateFacets = function() {

            // Zero out facet list
            if ($.isEmptyObject(pdh.facets)) {
                $facets.each(function() {
                    pdh.facets[$(this).text()] = 0;
                });
            } else { for (key in pdh.facets) { pdh.facets[key] = 0; } }
        
            // Count active tags
            $rows.each(function() { 
                var $row = $(this);
                if (!$row.hasClass("hidden")) {
                    $row.data("tags").split("|").forEach(function(val) {
                        pdh.facets[val] += 1;
                    })
                }
            });

            // Sort active facets by count
            const sorted = Object.entries(pdh.facets).sort(
                function(a, b) { return ((a[1] > b[1]) ? -1 : ((a[1] < b[1]) ? 1 : 0));
            });
            
            // Add facets to sidebar
            $facets.remove();
            sorted.forEach(function(val) {
                if (val[0].length > 0 && val[1] > 0) {
                    var li = document.createElement("li");
                    var a = document.createElement("a");
                    a.href = "/topics/" + val[0].replaceAll(" ", "-")
                    a.innerText = val[0];
                    if (pdh.selected.includes(val[0])) { a.classList.add("selected"); }
                    li.appendChild(a);
                    li.innerHTML += " (" + val[1] + ")";
                    $("ul.faceted").append(li);
                }
            });

            // Add handler
            $facets = $("ul.faceted").find("li");
            $facets.find("a").on("click", pdh.toggleFacet);
        }

        pdh.resizeIframe = function() {
            $("iframe").each(function(e) {
                var $this = $(this);
                var key = $(this).attr("src");
                if (!(key in pdh.iframes)) {
                    pdh.iframes[key] = $this.width() / $this.height();
                }              
                var aspectRatio = pdh.iframes[key];
                $this.attr("width", "100%");
                $this.attr("height", $(this).width() / aspectRatio);
            })
        }

        // Enable handlers
        // $("ul.collapsible li:has(ul) span.nav__sub-title").on("click", pdh.toggleSubmenu);
        $("ul.faceted a").on("click", pdh.toggleFacet);
        $("table.faceted tr td:nth-child(2) a").on("click", pdh.toggleFacet);
        $(window).on("resize", pdh.resizeIframe);

    }( window.pdh = window.pdh || {}, jQuery ));

    pdh.resizeIframe();
    pdh.updateFacets();

});