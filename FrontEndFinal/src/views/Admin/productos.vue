<template>
	<vx-card>
		<vs-table stripe title="Sectores" pagination max-items="7" search :data="arrayData" noDataText="No hay datos disponibles">
			<template slot="header">
			<vs-button @click="abrirForm=true" icon-pack="feather" icon="icon-plus-circle" icon-after>Nuevo</vs-button>
			</template>
				<template slot="thead">
					<vs-th >Nombre</vs-th>
					<vs-th >Descripción</vs-th>
					<vs-th >Existencia</vs-th>
					<vs-th >Precio</vs-th>
					<vs-th >Categoria</vs-th>
					<vs-th >Acciones</vs-th>
				</template>

				<template slot-scope="{data}">
					<vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">

						<vs-td :data="data[indextr].node.nombreProducto">
							{{data[indextr].node.nombreProducto}}
						</vs-td>

						<vs-td :data="data[indextr].node.Descripcion">
							{{data[indextr].node.Descripcion}}
						</vs-td>

						<vs-td :data="data[indextr].node.Existencia">
							{{data[indextr].node.Existencia}}
						</vs-td>
						<vs-td :data="data[indextr].node.Precio">
							{{data[indextr].node.Precio}}
						</vs-td>

						<vs-td :data="data[indextr].node.Categoria.nombreCategoria">
							{{data[indextr].node.Categoria.nombreCategoria}}
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
				title="Guardar Producto"
				accept-text= "Guardar"
				@accept="AgregarProducto"
				:active.sync="abrirForm"
				@cancel="close"
				@close="close"
				>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Nombre" v-model="nombre"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Descripcion" v-model="descripcion"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Existencia" v-model="existencia"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Precio" v-model="precio"></vs-input>
				<small>Categoria</small>
					<v-select name="Categoria" label="nombreCategoria" :options="listadoCategorias" v-model="categoria_id" :dir="$vs.rtl ? 'rtl' : 'ltr'" />
			</vs-prompt>

			<vs-prompt
				class="calendar-event-dialog"
				title="Editar Producto"
				accept-text= "Guardar"
				@accept="EditarProducto"
				:active.sync="abrirEditar"
				@cancel="close"
				@close="close"
				>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Nombre" v-model="nombreT"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Descripcion" v-model="descripcionT"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Existencia" v-model="existenciaT"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Precio" v-model="precioT"></vs-input>
				<small>Categoria</small>
					<v-select name="Categoria" label="nombreCategoria" :options="listadoCategorias" v-model="categoria_idT" :dir="$vs.rtl ? 'rtl' : 'ltr'" />
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
			listadoCategorias:[],
			abrirForm:false,
			abrirEditar:false,
			langHe: es,
			langEn: es,
			endDate: '',
			startDate: '',
			id: 0,
			nombre:0,
			descripcion: null,
			existencia:'',
			categoria:null,
			nombre:"",
			descripcion:"",
			existencia:"",
			precio:"",
			categoria_id:"",
			total:"",
			nombreT:"",
			descripcionT:"",
			existenciaT:"",
			precioT:"",
			categoria_idT:"",
			totalT:"",
			editarId:null,
			deleteId:null
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
				valor.nombreCategoria=valor.node.nombreCategoria
			}); 
			return tabla
		},
		getDate(datetime) {
			let date = new Date(datetime);
			let dateString = `${date.getFullYear()}/${date.getMonth() + 1}/${date.getDate()}`;
			return dateString;
		},
		Editar(datos){
			this.nombreT=datos.nombreProducto
			this.descripcionT=datos.Descripcion
			this.existenciaT=datos.Existencia
			this.precioT=datos.Precio
			let elementoE = ''
			let encontrado = false
			this.listadoCategorias.forEach(function(elemento, indice, array) {
				if (elemento.node.nombreCategoria==datos.Categoria.nombreCategoria)
					{
						elementoE=elemento
						encontrado=true
					}
				})
			this.categoria_idT = encontrado == true ? elementoE:{id:datos.Categoria,nombreCategoria:'No Existe'} 
			this.editarId=datos.id
			this.abrirEditar=true
			
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
							deleteProducto(input:{
								id: "${this.deleteId}"
							}){
								Producto{
								id
								nombreProducto
								Descripcion
								Existencia
								Precio
								nombreProducto
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
		async AgregarProducto(){
			try {
				var result = await axios({
					method: 'POST',
					url: 'https://publicacionfinal.herokuapp.com/graphql/',
					data: {
						query:`
						mutation{
						createProducto(input:{
								nombreProducto:"${this.nombre}",
								Descripcion:"${this.descripcion}",
								Existencia:${this.existencia},
								Precio:${this.precio},
								nombreCategoria:"${this.categoria_id.nombreCategoria}"
						}){
							Producto{
							id
							nombreProducto
							Descripcion
							Existencia
							Precio
							nombreProducto
							}
						}
						}
							`
							}
						})
						this.nombre=""
						this.descripcion=""
						this.existencia=0
						this.precio=0
						this.categoria_id=null
						this.index();
					} catch (error) {
						console.error(error)
					}

		},
		async EditarProducto(){
			try {
				var result = await axios({
					method: 'POST',
					url: 'https://publicacionfinal.herokuapp.com/graphql/',
					data: {
						query:`
							mutation{
							updateProducto(input:{
								id: "${this.editarId}",
								nombreProducto:"${this.nombreT}",
								Descripcion:"${this.descripcionT}",
								Existencia:${this.existenciaT},
								Precio:${this.precioT},
								nombreCategoria:"${this.categoria_idT.nombreCategoria}"
							}){
								Producto{
								id
								nombreProducto
								Descripcion
								Existencia
								Precio
								nombreProducto
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
							allProductos{
							edges{
								node{
								id,
								nombreProducto,
								Descripcion,
								Existencia,
								Precio,
								Categoria{
									id,
									nombreCategoria,
								}
								}
							}
							}
							}
							`
							}
						})
						// this.arrayData = result.data.data.todosProveedores
						this.arrayData = result.data.data.allProductos.edges
					} catch (error) {
						console.error(error)
					}
		},
		async index2(){
			try {
				var result = await axios({
					method: 'POST',
					url: 'https://publicacionfinal.herokuapp.com/graphql/',
					data: {
						query:`
							query{
							allCategorias{
							edges{
								node{
								id
								nombreCategoria
								}
							}
							}
							}
							`
							}
						})
						// this.arrayData = result.data.data.todosProveedores
						this.listadoCategorias = this.traerNombre(result.data.data.allCategorias.edges)
					} catch (error) {
						console.error(error)
					}
		},
	},
  	mounted(){
    	this.index();
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