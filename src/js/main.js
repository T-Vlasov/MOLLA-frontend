import $ from "jquery";
import 'slick-carousel';

$(function () {

    $('.top__slider').slick({
        dots:false,
        arrows:true,
        fade:true
    })
    $('.bottom__slider').slick({
        dots:false,
        arrows:false,
        fade:true
    })
    $('.top__slider .slick-arrow.slick-prev').on('click',function(){
        $('.bottom__slider').slick('slickPrev');
    })
    $('.top__slider .slick-arrow.slick-next').on('click',function(){
        $('.bottom__slider').slick('slickNext');
    })

    $('.menu__links-item__ort').on('click',function(e){
        e.preventDefault()
        $('.card-ort').removeClass('d-none');
        $('.card-game').addClass('d-none');
        $('.card-office').addClass('d-none');
        $('.menu__links-item__game').removeClass('menu__active');
        $('.menu__links-item__ort').addClass('menu__active');
        $('.menu__links-item__office').removeClass('menu__active');
    })


    $('.menu__links-item__game').on('click',function(e){
        e.preventDefault()
        $('.card-game').removeClass('d-none');
        $('.card-ort').addClass('d-none');
        $('.card-office').addClass('d-none');
        $('.menu__links-item__game').addClass('menu__active');
        $('.menu__links-item__ort').removeClass('menu__active');
        $('.menu__links-item__office').removeClass('menu__active');
    })

    $('.menu__links-item__office').on('click',function(e){
        e.preventDefault()
        $('.card-office').removeClass('d-none');
        $('.card-ort').addClass('d-none');
        $('.card-game').addClass('d-none');
        $('.menu__links-item__game').removeClass('menu__active');
        $('.menu__links-item__ort').removeClass('menu__active');
        $('.menu__links-item__office').addClass('menu__active');
    })

})

$(function() {
    $('.categories__item-ort').on('click',function(){
        $(window).on('load',function(){
            $('.ort-chairs').removeClass('d-none');
            $('.game-chairs').addClass('d-none');
            $('.office-chairs').addClass('d-none');
        })
    })
})

$(function() {
    $('.buy').on('click',function(){
        $(this).closest('.buttons').find('.buy').addClass('d-none');
        $(this).closest('.buttons').find('.count').removeClass('d-none');
        $(this).closest('.buttons').find('.plus').removeClass('d-none');
        $(this).closest('.buttons').find('.minus').removeClass('d-none');
    })
    
    $('.plus').on('click',function(){
        $(this).closest('.buttons').find('.count').html(+$(this).closest('.buttons').find('.count').html() + 1)
    })
    
    $('.minus').on('click',function(){

        const counterDiv = $(this).closest('.buttons')
        const counter = counterDiv.find('.count')

        if (parseInt(counterDiv.find('.count').html())>1){
            counter.html(+counterDiv.find('.count').html() - 1)
        }
        else {
            $(this).closest('.buttons').find('.buy').removeClass('d-none');
            $(this).closest('.buttons').find('.count').addClass('d-none');
            $(this).closest('.buttons').find('.plus').addClass('d-none');
            $(this).closest('.buttons').find('.minus').addClass('d-none');
        }
    })
})

$(function() {
    $('.buy').on('click',function(){

        const card = $(this).closest('.card')

        const productInfo = {
            imgSrc: card.find('.card__image').attr('src'),
            title: card.find('.card__title-cart').html(),
            description: card.find('.card__description-cart').html(),
            description2: card.find('.card__description-cart2').html(),
            price: card.find('.card__price-cart').html(),
            count: card.find('.count').html(),
        }

        var cartItemHTML = `
        <div class="products__card">
            <div class="card__img">
            <a href="office-chair-1.html"><img src="${productInfo.imgSrc}" alt="" class="card__image"></a>
            </div>
            <div class="card__info">
            <h4 class="card__title">
                <a class="card__title card__title-cart" href="office-chair-1.html">${productInfo.title}</a>
            </h4>
            <p class="card__description">
                <a class="card__description card__description-cart" href="office-chair-1.html">${productInfo.description}</a>
            </p>
            <p class="card__description">
                <a class="card__description card__description-cart2" href="office-chair-1.html">${productInfo.description2}</a>
            </p>
            <h5 class="card__price">
                <a class="card__price card__price-cart" href="office-chair-1.html">${productInfo.price}</a>
            </h5>
            <div class="buttons">
                <button class="buy">
                Купить
                </button>
                <div class="counter">
                <button class="plus d-none">
                    +
                </button>
                <div class="count d-none">${productInfo.count}</div>
                <button class="minus d-none">
                    -
                </button>
                </div>
                <button class="like"></button>
            </div>
            <div class="stars">
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star checked"></span>
            </div>
            </div>
        </div>`;

        $('.products').before(cartItemHTML)
        
    })
    $(function(e) {
        $('.cart').on('click',function(){
            e.preventDefault()
            $('.products').before(cartItemHTML)
        })
    })
})
