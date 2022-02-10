(function(){"use strict";const select=(el,all=!1)=>{el=el.trim()
    if(all){return[...document.querySelectorAll(el)]}else{return document.querySelector(el)}}
    const on=(type,el,listener,all=!1)=>{let selectEl=select(el,all)
    if(selectEl){if(all){selectEl.forEach(e=>e.addEventListener(type,listener))}else{selectEl.addEventListener(type,listener)}}}
    const onscroll=(el,listener)=>{el.addEventListener('scroll',listener)}
    const scrollto=(el)=>{let header=select('#header')
    let offset=header.offsetHeight
    let elementPos=select(el).offsetTop
    window.scrollTo({top:elementPos-offset,behavior:'smooth'})}
    let selectHeader=select('#header')
    if(selectHeader){const headerScrolled=()=>{if(window.scrollY>100){selectHeader.classList.add('header-scrolled')}else{selectHeader.classList.remove('header-scrolled')}}
    window.addEventListener('load',headerScrolled)
    onscroll(document,headerScrolled)}
    let backtotop=select('.back-to-top')
    if(backtotop){const toggleBacktotop=()=>{if(window.scrollY>100){backtotop.classList.add('active')}else{backtotop.classList.remove('active')}}
    window.addEventListener('load',toggleBacktotop)
    onscroll(document,toggleBacktotop)}
    on('click','.mobile-nav-toggle',function(e){select('#navbar').classList.toggle('navbar-mobile')
    this.classList.toggle('bi-list')
    this.classList.toggle('bi-x')})
    on('click','.navbar .dropdown > a > i',function(e){if(select('#navbar').classList.contains('navbar-mobile')){e.preventDefault()
    this.parentElement.nextElementSibling.classList.toggle('dropdown-active')}},!0)
    on('click','.scrollto',function(e){if(select(this.hash)){e.preventDefault()
    let navbar=select('#navbar')
    if(navbar.classList.contains('navbar-mobile')){navbar.classList.remove('navbar-mobile')
    let navbarToggle=select('.mobile-nav-toggle')
    navbarToggle.classList.toggle('bi-list')
    navbarToggle.classList.toggle('bi-x')}
    scrollto(this.hash)}},!0)
    window.addEventListener('load',()=>{if(window.location.hash){if(select(window.location.hash)){scrollto(window.location.hash)}}});let skilsContent=select('.skills-content');if(skilsContent){new Waypoint({element:skilsContent,offset:'80%',handler:function(direction){let progress=select('.progress .progress-bar',!0);progress.forEach((el)=>{el.style.width=el.getAttribute('aria-valuenow')+'%'})}})}
    new Swiper('.clients-slider',{speed:400,loop:!0,autoplay:{delay:5000,disableOnInteraction:!1},slidesPerView:'auto',pagination:{el:'.swiper-pagination',type:'bullets',clickable:!0},breakpoints:{320:{slidesPerView:2,spaceBetween:40},480:{slidesPerView:3,spaceBetween:60},640:{slidesPerView:4,spaceBetween:80},992:{slidesPerView:6,spaceBetween:120}}});window.addEventListener('load',()=>{AOS.init({duration:1000,easing:'ease-in-out',once:!0,mirror:!1})})})()