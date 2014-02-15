$(document).ready(function(){
    //"bootstrapize" the tables
    $("table").each(function(){$(this).attr("border", "0").addClass("table").addClass("table-bordered")})

    //replace href="#" links to #id-of-the-first-section, so that the scroll
    //stuff works as expected.
    $("li.scroll > a[href='#']").filter(":not(.dropdown-toggle)").each(function(){
        if(typeof($(this).data().toogle) == 'undefined'){ this.href = "#" + $(".section")[0].id }
    
    })

    //add some smooth scrolling to local refs.
    var offsetHeight = 51;
    $("li.scroll > a[href^='#']").filter(":not(.dropdown-toggle)").on('click', 
        function(e) {
             e.preventDefault();
             var pos = document.getElementById(this.hash.replace("#","")).offsetTop
             $('html, body').animate({ scrollTop: pos - offsetHeight}, 600); });

    //hero-unit remove the container class added by the ..container:: directive
    $(".hero-unit").each(function(){ $(this).removeClass("container")})

    //$(".hero-unit > p > a").each(function(){ $(this).addClass("btn")})

    //convert the first paragraph to a header.
    var o = $(".hero-first-h2 > p").filter(":first()")
    var d = $("<h2></h2>")
    d.append(o.contents())
    o.replaceWith(d)

    //relocate-h1 : moves the previous H1 element inside the hero unit, as
    //docutils does not allows a heading inside a contaner. 
    $(".hero-relocate-h1").each(function(){ $(this).prev('h1').prependTo($(this)) });

    //The icon role produces <em> elements, <i> are strictly graphical. 
    //BTW, I couldn't produce <i> elements with docutils in less than 4 lines..
    $("em.icon-holder").each(function(){ 
        var newtag = $("<i></i>")
        newtag.attr('class', $(this).attr('class'))
        $(this).replaceWith(newtag)
    })

    //external links on new window
    if (typeof  window.new_page != 'undefined'){
        $('a.reference.external').each(function() {
            $(this).click(function(event) { 
                event.preventDefault(); event.stopPropagation();window.open(this.href, '_blank');
            });
        });
    };
    //If the document was loaded as doc#section scroll offsetHeight + section's
    //offsetTop.
    if ($(location).attr('href').indexOf('#') !== -1) {
        var name = $(location).attr('href').split("#")[1]
        var pos = document.getElementById(name).offsetTop - offsetHeight
        $("html, body").animate({ scrollTop: pos }, 200);
    }
    
})
