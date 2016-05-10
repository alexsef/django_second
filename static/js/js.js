window.onload=function(){
    jQuery('ul.nav > li').hover(function() {
    jQuery(this).find('.dropdown-menu').stop(true, true).fadeIn();
}, function() {
    jQuery(this).find('.dropdown-menu').stop(true, true).fadeOut();
})
    // $(".navbar").autoHidingNavbar('setDisableAutohide', true)
}
