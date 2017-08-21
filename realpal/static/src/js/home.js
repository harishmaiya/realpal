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

   $('.header .row .purchase').mouseover(function(){
       $('.purchase a').children('.works').stop().slideDown()
   });

    $('.header .row .purchase').mouseout(function(){
       $('.purchase a').children('.works').stop().slideUp()
   });

   $('.header .row .own').mouseover(function(){
       $('.own a').children('.works').stop().slideDown()
   });

    $('.header .row .own').mouseout(function(){
       $('.own a').children('.works').stop().slideUp()
   });





});
