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

						<vs-td :data="data[indextr].nombre">
							{{data[indextr].nombre}}
						</vs-td>

						<vs-td :data="data[indextr].rol">
							{{data[indextr].rol}}
						</vs-td>
						<vs-td>
							<div class="flex items-center">
								<vx-tooltip text="Editar"><vs-button @click="Editar(data[indextr])" radius color="dark" type="flat" icon="edit" size="large">  </vs-button>  </vx-tooltip>
								<vx-tooltip text="Eliminar"><vs-button @click="Eliminar(data[indextr].id)" radius color="dark" type="flat" icon="delete" size="large"> </vs-button></vx-tooltip>
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
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Password" v-model="password"></vs-input>
				<small>Rol</small>
					<v-select name="Categoria" label="nombre" :options="listadoRoles" v-model="rol_id" :dir="$vs.rtl ? 'rtl' : 'ltr'" />
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
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Password" v-model="passwordT"></vs-input>
				<small>Rol</small>
					<v-select name="Categoria" label="nombre" :options="listadoRoles" v-model="rol_idT" :dir="$vs.rtl ? 'rtl' : 'ltr'" />
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
			console.log(data)
			this.abrirEditar=true
			this.usuarioT=data.nombre
			this.passwordT=data.password
			this.rol_idT=data.rol_id
		},
		editarUsuario(){
			console.log('confirmar editar')
		},
		Eliminar(id){
			console.log(id)
			let titulo = '';
			let color = '';

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
		delete(){
			console.log('confirmar Eliminar')
		},
		agregarUsuario(){
			console.log('agregando usuario')
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
			let me = this;
			const response = await axios.get(`/api/sector/get?completo=true`)
			.then(function (response) {
				var respuesta= response.data;
				me.arrayData = respuesta.sectores.data;
				me.arrayData = me.traerNombre(me.arrayData)
			})
			.catch(function (error) {
				console.log(error);
			});
		},
		index2(){
			this.arrayData = [
				{id:1,nombre:'Primero',password:'Uno',rol_id:1},
				{id:2,nombre:'Tercero',password:'Dos',rol_id:2},
				{id:3,nombre:'Cuardo',password:'Tres',rol_id:3},
				{id:4,nombre:'Quinto',password:'Cuatro',rol_id:4}
			]
			this.listadoRoles	=[
				{id:1,nombre:'Gas'},
				{id:2,nombre:'Leche'},
				{id:3,nombre:'Comida'},
			]
		},
	},
  	mounted(){
    	//this.index();
		this.index2();
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

