<template>
  <div id="index">
    <DataManager :inputTexts="texts" ref="manager"></DataManager>
    <Canvas :inputTexts="texts" ref="canvas"></Canvas><br>
    <textarea v-model="texts" placeholder="input here"/><br>
    <button type="submit" @click="prevSlide">前のスライドへ</button>
    <button type="submit" @click="nextSlide">次のスライドへ</button>
    <!--<input type="range" min="0" v-bind:max="slideLength" step="1" v-model="number">-->
    <p>texts: {{ texts }}</p>
    <p>index: {{ index }}</p>
    <button type="submit" @click="startAnimation">再生</button>
  </div>
</template>

<script>
import DataManager from './DataManager.vue'
import Canvas from './Canvas.vue'
export default {
  components: {
    DataManager,
    Canvas
  },
  data () {
    return {
      texts: '',
      index: 0
    }
  },
  methods: {
    nextSlide () {
      this.$refs.manager.setSlideTexts(this.index)
      this.index += 1
      this.texts = this.$refs.manager.getSlideTexts(this.index)
    },
    prevSlide () {
      this.$refs.manager.setSlideTexts(this.index)
      if (this.index > 0) {
        this.index -= 1
      }
      this.texts = this.$refs.manager.getSlideTexts(this.index)
    },
    startAnimation () {
      this.$refs.canvas.startAnimation(this.$refs.manager.getSlides())
    }
  }
}
</script>
