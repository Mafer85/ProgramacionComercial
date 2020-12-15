<template>
  <div>
    <vs-input
        name="email"
        icon-no-border
        icon="icon icon-user"
        icon-pack="feather"
        label-placeholder="Usuario"
        v-model="usuario"
        class="w-full"/>
    <span class="text-danger text-sm">{{ errors.first('usuario') }}</span>

    <vs-input
        type="password"
        name="password"
        icon-no-border
        icon="icon icon-lock"
        icon-pack="feather"
        label-placeholder="Password"
        v-model="password"
        class="w-full mt-8" />
    <span class="text-danger text-sm">{{ errors.first('password') }}</span>

    <div class="flex flex-wrap justify-between mb-3 mt-8">
      <vs-button @click="loginJWT">Login</vs-button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      usuario: '',
	  password:'',
	  arrayData:[]
    }
  },
  methods: {
    checkLogin () {
      if (this.$store.state.auth.isUserLoggedIn()) {
        this.$vs.notify({
          title: 'Login Attempt',
          text: 'You are already logged in!',
          iconPack: 'feather',
          icon: 'icon-alert-circle',
          color: 'warning'
        })

        return false
      }
      return true
    },
    loginJWT () {
		let encontrado = false
		for (let i in this.arrayData) {
			let elemento = this.arrayData[i].node

			if (this.usuario === elemento.usuarios){
				if (this.password === elemento.Contrasenia)
				{
					encontrado = true
					localStorage.setItem('Rol', elemento.Roles)
					localStorage.setItem('Usuario', elemento.usuarios)
					this.$vs.notify({
					color:'success',
						title:`Bienvenido`,
						text:`Bienvenido nuevamente ${this.usuario}`
					})
					this.$router.push('/Ventas/ventas');
				}
			}
		}
		if (encontrado==false){
			this.$vs.notify({
			color:'danger',
				title:`Error`,
				text:`Datos incorrectos, intente nuevamente`
			})
		}
	},
	async index(){
	try {
		var result = await axios({
			method: 'POST',
			url: 'https://publicacionfinal.herokuapp.com/graphql/',
			data: {
				query:`
					query{
					allEmpleados{
					edges{
						node{
						id,
						usuarios,
						Contrasenia,
						Roles,
						}
					}
					}
					}
					`
					}
				})
				this.arrayData = result.data.data.allEmpleados.edges
			} catch (error) {
				console.error(error)
			}
	this.listadoRoles	=[
		{id:1,nombre:'Administrador'},
		{id:2,nombre:'Vendedor'},
	]
},
  },
  mounted(){
	this.index();
  }
}

</script>

