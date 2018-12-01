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
      return this.Slides[num]
    },
    // setter
    setSlideTexts (mum) {
    },
    // 変更
    changeSlideTexts (num) {
    },
    // 追加
    addNewSlide () {
    },
  }
}
</script>
