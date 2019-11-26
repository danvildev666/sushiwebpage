var btnMenu = document.getElementById('btn-menu');
var nav = document.getElementById('nav');
btnMenu.addEventListener('click',function(){
   nav.classList.toggle('muestrate');
});
/*******LOADER*********/
window.onload=function(){
   /**/
   $('#preloader').fadeOut();
}

  $(document).ready(function(){

    $('.carousel').carousel();

  });
  
  $('.toggle').click(function(){
   $('.formulario').animate({
       height: "toggle",
       'padding-top': 'toggle',
       'padding-bottom': 'toggle',
       opacity: 'toggle'
   }, "slow");
});  
  



