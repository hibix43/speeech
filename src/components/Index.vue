<template>
  <div id="index">
    <DataManager :inputTexts="texts" ref="manager"></DataManager>
    <Canvas :inputTexts="texts" ref="canvas"></Canvas>
    <textarea v-model="texts" placeholder="input here"/>
    <div class="row">
      <button class="btn six columns" type="submit" @click="prevSlide">前のスライドへ</button>
      <button class="btn six columns" type="submit" @click="nextSlide">次のスライドへ</button>
    </div>
    <div class="row">
      <button class="btn four columns" type="submit" @click="startAnimation(0)">最初のスライドから再生</button>
      <button class="btn four columns" type="submit" @click="startAnimation(index)">現在のスライドから再生</button>
      <button class="btn four columns" type="submit" @click="stopAnimation">停止</button>
    </div>
    <button class="btn complete-btn" type="submit">完成させてツイートする</button>
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

<style scoped>
textarea {
  min-width: 320px;
  min-height: 180px;
  margin: 16px 0;
}
.row {
  margin: 16px 64px;
}
.btn {
  font-size: 1em;
  font-weight: bold;
  background-color: #666;
  color: #fff;
}
.complete-btn {
  font-size: 1.5em;
  border-radius: 0;
  margin: 8px 0;
  width: 320px;
  height: 60px;
  background-color: #00bbee;
  color: #fff;
  border: 1px solid #fff;
  box-shadow: 0 0 4px #00bbee;
}
</style>
