<template>
  <div id="index">
    <DataManager :inputTexts="texts" ref="manager"></DataManager>
    <Canvas :inputTexts="texts" ref="canvas"></Canvas><br>
    <textarea v-model="texts" placeholder="input here"/><br>
    <button type="submit" @click="prevSlide">前のスライドへ</button>
    <button type="submit" @click="nextSlide">次のスライドへ</button>
    <p>texts: {{ texts }}</p>
    <div>
      <p>Min: 0</p>
      <input type="range" min=0 v-bind:max="indexMax" step=1 v-model="index">
      <p>Max: {{ indexMax }}</p>
      <p>index: {{ index }}</p>
    </div>
    <button type="submit" @click="startAnimation(0)">最初のスライドから再生</button>
    <button type="submit" @click="startAnimation(index)">現在のスライドから再生</button>
    <button type="submit" @click="stopAnimation">停止</button>
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
      index: 0,
      indexMax: 0
    }
  },
  watch: {
    index () {
      this.texts = this.$refs.manager.getSlideTexts(this.index)
    }
  },
  methods: {
    nextSlide () {
      this.$refs.manager.setSlideTexts(this.index)
      this.index += 1
      this.texts = this.$refs.manager.getSlideTexts(this.index)
      // 新たに追加したら、indexMaxを更新
      this.indexMax = this.$refs.manager.getSlides().length
    },
    prevSlide () {
      this.$refs.manager.setSlideTexts(this.index)
      if (this.index > 0) {
        this.index -= 1
      }
      this.texts = this.$refs.manager.getSlideTexts(this.index)
    },
    startAnimation (startIndex) {
      this.$refs.canvas.startAnimation(this.$refs.manager.getSlides(), startIndex)
    },
    stopAnimation () {
      this.$refs.canvas.stopAnimation()
    }
  }
}
</script>
