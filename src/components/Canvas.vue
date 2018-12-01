<template>
  <canvas width="400" height="300" class="canvas"></canvas>
</template>

<script>
export default {
  props: {
    inputTexts: ''
  },
  watch: {
    inputTexts () {
      this.draw(this.inputTexts)
    }
  },
  methods: {
    draw (texts) {
      const context = this.ctx
      const canvasWidth = 400
      const canvasHeight = 300
      const fontSize = 36

      // 初期化
      context.clearRect(0, 0, canvasWidth, canvasHeight)
      // 背景色を黒にして塗りつぶす
      context.fillStyle = '#000'
      context.fillRect(0, 0, canvasWidth, canvasHeight)

      // フォント設定
      context.textAlign = 'center'
      context.font = 'bold ' + fontSize + 'px Arial, meiryo, sans-serif'
      context.fillStyle = '#fff'

      // 書きだす
      context.beginPath()

      // 描画
      context.fillText(texts, canvasWidth / 2, canvasHeight / 2)
    }
  },
  mounted () {
    this.ctx = this.$el.getContext('2d')
    this.draw(this.inputTexts)
  }
}
</script>

<style>
 .canvas {
     border: 1px solid #333;
 }
</style>
