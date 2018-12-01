<template>
  <p>{{ Slides }}</p>
</template>

<script>
export default {
  props: {
    inputTexts: ''
  },
  data () {
    return {
      Slides: []
    }
  },
  methods: {
    // getter
    getSlideTexts (slideIndex) {
      if (slideIndex > this.Slides.length - 1) {
        return ''
      } else {
        return this.Slides[slideIndex]
      }
    },
    // setter
    setSlideTexts (slideIndex) {
      if (slideIndex > this.Slides.length - 1) {
        this.addNewSlide()
      } else if (slideIndex < this.Slides.length) {
        this.changeSlideTexts(slideIndex)
      }
      console.log(this.Slides)
    },
    // 変更
    changeSlideTexts (slideIndex) {
      this.Slides[slideIndex] = this.inputTexts
    },
    // 追加
    addNewSlide () {
      this.Slides.push(this.inputTexts)
    }
  }
}
</script>
