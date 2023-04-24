<script setup>
const name = "Leo"
const StyleColor = "color: blue"
const bandera = false
</script>

<template>
  <h1>Hola {{ name.toUpperCase() }}</h1>
  <h2>soy azul</h2>
  <h1 v-if="bandera">helo</h1>
  <h1 v-else="bandera">nada</h1>
</template>

<style>
h1{
  color: aquamarine;
}
</style>
