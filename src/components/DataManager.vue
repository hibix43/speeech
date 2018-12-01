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
      if (num > this.Slides.length - 1) {
        return ''
      } else {
        return this.Slides[num]
      }
    },
    // setter
    setSlideTexts (num) {
      if (num > this.Slides.length - 1) {
        this.addNewSlide()
      } else if (num < this.Slides.length) {
        this.changeSlideTexts(num)
      }
      console.log(this.Slides)
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
