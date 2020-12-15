<template>
	<vx-card>
		<vs-table stripe title="Sectores" pagination max-items="7" search :data="arrayData" noDataText="No hay datos disponibles">
			<template slot="header">
			<vs-button @click="abrirForm=true" icon-pack="feather" icon="icon-plus-circle" icon-after>Nuevo</vs-button>
			</template>
				<template slot="thead">
					<vs-th> Usuario </vs-th>
					<vs-th> Rol </vs-th>
					<vs-th> Acciones </vs-th>
				</template>

				<template slot-scope="{data}">
					<vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">

						<vs-td :data="data[indextr].node.usuarios">
							{{data[indextr].node.usuarios}}
						</vs-td>

						<vs-td :data="data[indextr].node.Roles">
							{{data[indextr].node.Roles}}
						</vs-td>
						<vs-td>
							<div class="flex items-center">
								<vx-tooltip text="Editar"><vs-button @click="Editar(data[indextr].node)" radius color="dark" type="flat" icon="edit" size="large">  </vs-button>  </vx-tooltip>
								<vx-tooltip text="Eliminar"><vs-button @click="Eliminar(data[indextr].node.id)" radius color="dark" type="flat" icon="delete" size="large"> </vs-button></vx-tooltip>
							</div>
						</vs-td>
					</vs-tr>
				</template>
			</vs-table>

			<vs-prompt
				class="calendar-event-dialog"
				title="Agregar Producto"
				accept-text= "Guardar"
				@accept="agregarUsuario"
				:active.sync="abrirForm"
				@cancel="close"
				@close="close"
				>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Usuario" v-model="usuario"></vs-input>
				<vs-input name="event-name" v-validate="'required'" type="password" class="w-full mt-8" label-placeholder="Password" v-model="password"></vs-input>
				<small>Rol</small>
					<v-select label="nombre" :options="listadoRoles" v-model="rol_id" :dir="$vs.rtl ? 'rtl' : 'ltr'" />
			</vs-prompt>
			<vs-prompt
				class="calendar-event-dialog"
				title="Editar Producto"
				accept-text= "Guardar"
				@accept="editarUsuario"
				:active.sync="abrirEditar"
				@cancel="close"
				@close="close"
				>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Usuario" v-model="usuarioT"></vs-input>
				<vs-input name="event-name" type="password" v-validate="'required'" class="w-full mt-8" label-placeholder="Password" v-model="passwordT"></vs-input>
				<small>Rol</small>
					<v-select label="nombre" :options="listadoRoles" v-model="rol_idT" :dir="$vs.rtl ? 'rtl' : 'ltr'" />
			</vs-prompt>

	</vx-card>
</template>



<script>
import VueApexCharts from 'vue-apexcharts'
import StatisticsCardLine from '@/components/statistics-cards/StatisticsCardLine.vue'
//import analyticsData from './ui-elements/card/analyticsData.js'
import ChangeTimeDurationDropdown from '@/components/ChangeTimeDurationDropdown.vue'
import VxTimeline from '@/components/timeline/VxTimeline'
// import Formulariosector from './formulariosector.vue'
import vSelect from 'vue-select'
import axios from 'axios'
import Datepicker from 'vuejs-datepicker'
import { es } from 'vuejs-datepicker/src/locale'


export default {
	data () {
		return {
			//Aqui van a guardar todas su variables.
			arrayData: [],
			listadoRoles:[],
			abrirForm:false,
			abrirEditar:false,
			rol_idT:null,
			rol_id:null,
			id: 0,
			usuario:'',
			password:'',
			usuarioT:'',
			passwordT:'',
			editarId:null,
			deleteId:null,
		}
	},
	components: {
		VueApexCharts,
		StatisticsCardLine,
		ChangeTimeDurationDropdown,
		VxTimeline,
		Datepicker,
		vSelect,
	},
	methods: {
		traerNombre(tabla){
			tabla.forEach(function(valor, indice, array){
				valor.aldea_nombre=valor.aldea.nombre
			}); 
			return tabla
		},
		getDate(datetime) {
			let date = new Date(datetime);
			let dateString = `${date.getFullYear()}/${date.getMonth() + 1}/${date.getDate()}`;
			return dateString;
		},
		Agregar(){
			this.abrirForm=true
		},
		Editar(data){
			this.usuarioT=data.usuarios
			this.passwordT=data.Contrasenia
			this.editarId=data.id
			let elementoE = ''
			let encontrado = false
			this.listadoRoles.forEach(function(elemento, indice, array) {
				if (elemento.nombre==data.Roles)
					{
						elementoE=elemento
						encontrado=true
					}
				})
			this.rol_idT = encontrado == true ? elementoE:{id:data.Roles,nombre:'No Existe'}
			this.abrirEditar=true
		},
		async editarUsuario(){
			try {
				var result = await axios({
					method: 'POST',
					url: 'https://publicacionfinal.herokuapp.com/graphql/',
					data: {
						query:`
								mutation{
									updateEmpleado(input:{
									id: "${this.editarId}",
									usuarios:"${this.usuarioT}",
									Contrasenia:"${this.passwordT}",
									Roles:"${this.rol_idT.nombre}"
								}){
									Empleado{
									id
									usuarios
									Contrasenia
									Roles
									}
								}
								}
							`
							}
						})
						this.index();
					} catch (error) {
						console.error(error)
					}
		},
		Eliminar(id){
			let titulo = '';
			let color = '';
			this.deleteId=id
			this.$vs.dialog({
				type:'confirm',
				color: 'danger',
				title: 'Eliminar Producto',
				text: '¿Está seguro de eliminar el producto?',
				accept: this.delete,
				cancel: this.close,
				acceptText: 'Aceptar',
				cancelText: 'Cancelar',
			})
		},
		async delete(){
			try {
				var result = await axios({
					method: 'POST',
					url: 'https://publicacionfinal.herokuapp.com/graphql/',
					data: {
						query:`
							mutation{
								deleteEmpleado(input:{
								id: "${this.deleteId}"
							}){
								Empleado{
								id
								usuarios
								Contrasenia
								Roles
								}
							}
							}
							`
							}
						})
						this.index();
					} catch (error) {
						console.error(error)
					}
		},
		async agregarUsuario(){
			try {
				var result = await axios({
					method: 'POST',
					url: 'https://publicacionfinal.herokuapp.com/graphql/',
					data: {
						query:`
								mutation{
								createEmpleado(input:{
									usuarios:"${this.usuario}"
									Contrasenia:"${this.password}",
									Roles:"${this.rol_id.nombre}"
								}){
									Empleado{
									id
									usuarios
									Contrasenia
									Roles
									}
								}
								}
							`
							}
						})
						this.index();
					} catch (error) {
						console.error(error)
					}
					this.usuario=""
					this.password=""
					this.rol_id=null
		},
		close(){
			let titulo = "Cancelado"
			let texto = "Se cancelo el ingreso"
			this.$vs.notify({
			color:'danger',
			title:`${titulo}`,
			text:`${texto}`
			})
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

<style lang="scss">
#dashboard-analytics {
  .greet-user{
    position: relative;
    .decore-left{
      position: absolute;
      left:0;
      top: 0;
    }
    .decore-right{
      position: absolute;
      right:0;
      top: 0;
    }
  }
  @media(max-width: 576px) {
    .decore-left, .decore-right{
      width: 140px;
    }
  }
}
</style>

