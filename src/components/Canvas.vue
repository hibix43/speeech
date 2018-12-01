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
      const lineHeight = 1.2
      // テキストを改行で分割
      let lines = texts.split('\n')

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

      // 改行を反映
      for (let i = 0; i <= lines.length; i++) {
        let line = lines[i]
        let addY = fontSize * lineHeight * i
        if (line !== undefined) {
          // 描画
          context.fillText(line, canvasWidth / 2, canvasHeight / 2 + addY)
        }
      }
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
