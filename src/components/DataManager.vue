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
    getSlideTexts (num) {
      if (num > this.Slides.length) {
        return ''
      } else {
        return this.Slides[num]
      }
    },
    // setter
    setSlideTexts (num) {
      if (num > this.Slides.length) {
        this.addNewSlide()
      } else {
        this.changeSlideTexts(num)
      }
    },
    // 変更
    changeSlideTexts (num) {
      this.Slides[num] = this.inputTexts
    },
    // 追加
    addNewSlide () {
      this.Slides.push(this.inputTexts)
    }
  }
}
</script>
