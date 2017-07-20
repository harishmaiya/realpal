/*global $, jQuery, alert */

$(document).ready(function () {
    
    $('.header .row').height($(window).height());
    
    $(window).resize(function(){
        
    $('.header .row').height($(window).height());
    });
    
   $('.header .row .prepare').mouseover(function(){
       $('.prepare a').children('.works').stop().slideDown()
   });
    
    $('.header .row .prepare').mouseout(function(){
       $('.prepare a').children('.works').stop().slideUp()
   });
    
   $('.header .row .buy').mouseover(function(){
       $('.buy a').children('.works').stop().slideDown()
   });
    
    $('.header .row .buy').mouseout(function(){
       $('.buy a').children('.works').stop().slideUp()
   });
    
   $('.header .row .live').mouseover(function(){
       $('.live a').children('.works').stop().slideDown()
   });
    
    $('.header .row .live').mouseout(function(){
       $('.live a').children('.works').stop().slideUp()
   });
   
   
    
       
    
});