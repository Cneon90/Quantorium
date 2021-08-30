const swiper = new Swiper('.swiper-container', {
  // Optional parameters

  loop: true,
        grabCursor: false,
		effect: 'fade',
        cubeEffect: {
          shadow: true,
          slideShadows: true,
          shadowOffset: 20,
          shadowScale: 0.94,
        },

        pagination: {
          el: ".swiper-pagination",
        },

		navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

	//slidesPerView: 1,
	//spaceBetween:2,

	autoplay:{

	   delay:2000,
	   disableOnInteraction:false
	},

	speed:1000,
});