<template>
  <div class="content">
    <AddPlayerForm />
    <AddGameForm />
    <GamesList />
    <br>
  </div>
</template>

<script>
import AddPlayerForm from './components/AddPlayerForm.vue';
import AddGameForm from './components/AddGameForm.vue';
import GamesList from './components/GamesList.vue'

export default {
  name: 'App',
  components: {
    AddPlayerForm,
    AddGameForm,
    GamesList,
  }
}
</script>
