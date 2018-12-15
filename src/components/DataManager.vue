<template>
  <div>
  </div>
</template>

<script>
export default {
  props: {
    inputTexts: ''
  },
  data () {
    return {
      Slides: Array(10)
    }
  },
  methods: {
    getSlides () {
      return this.Slides
    },
    // getter
    getSlideTexts (slideIndex) {
      return this.Slides[slideIndex]
    },
    // setter
    setSlideTexts (slideIndex) {
      /*
      if (slideIndex > this.Slides.length - 1) {
        this.addNewSlide()
      } else if (slideIndex < this.Slides.length) {
        this.changeSlideTexts(slideIndex)
      }
      console.log(this.Slides)
      */
      this.changeSlideTexts(slideIndex)
    },
    // 変更
    changeSlideTexts (slideIndex) {
      this.Slides[slideIndex] = this.inputTexts
    }
    // 追加
    /*
    addNewSlide () {
      this.Slides.push(this.inputTexts)
    }
    */
  }
}
</script>
