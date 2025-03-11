$(document).ready(function() {

    (function(pdh, $, undefined) {

        // Public variables
        pdh.selected = [];
        pdh.iframes = {};
        $rows = $("table").find("tr:has(td)");
        $facets = $("ul.faceted").find("li");

        // Public methods
        pdh.toggleSubmenu = function(e) {
            var $this = $(this);
            $this.off("click");
            e.preventDefault();
            console.log($this.next());
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
            $facets.removeClass("hidden");
            $facets.find("a").removeClass("selected");
            if (pdh.selected.length !== 0) {
                // Hide rows that do not match
                var available = [];
                var visible = {};
                $rows.each(function() { 
                    var $row = $(this);
                    var tags = [];
                    $row.find("a").each(function() { tags.push($(this).text()); })
                    if (tags.filter(x => pdh.selected.includes(x)).length == pdh.selected.length) {
                        available = available.concat(tags);
                    } else { $row.addClass("hidden"); } 
                });
                available = [...new Set(available)];
                $facets.each(function() {
                    var $facet = $(this);
                    if (!available.includes($facet.text())) {
                        $facet.addClass("hidden");
                    } else if (pdh.selected.includes($facet.text())) {
                        $facet.find("a").addClass("selected");
                    }
                });
            }
            $this.on("click", pdh.toggleFacet);
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

});