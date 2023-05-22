<template>
  <div>
    <h2>Добавить игрока</h2>
    <form @submit.prevent="handleSubmit">
      <p>
        <label for="name">Имя</label>:
        <input type="text" id="name" v-model="name" required>
      </p>
      <p>
        <label for="surname">Фамилия</label>:
        <input type="text" id="surname" v-model="surname" required>
      </p>
      <button type="submit">Создать</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      surname: ''
    };
  },
  methods: {
    async handleSubmit() {
      const playerData = {
        name: this.name,
        surname: this.surname
      }
      try {
        const response = await this.$http.post('players', playerData);
        console.log(response.data);
      }
      catch (error) {
        console.error(error);
      }
    }
  }
};
</script>