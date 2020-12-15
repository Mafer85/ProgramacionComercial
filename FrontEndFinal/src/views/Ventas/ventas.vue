<template>
	<vx-card>
		<vs-table stripe title="Sectores" pagination max-items="7" search :data="arrayData" noDataText="No hay datos disponibles">
			<template slot="header">
				<vs-button @click="abrirForm=true" icon-pack="feather" icon="icon-plus-circle" icon-after>Nuevo</vs-button>
			</template>
				<template slot="thead">
					<vs-th >Serie</vs-th>
					<vs-th >Cliente</vs-th>
					<vs-th >NIT</vs-th>
					<vs-th >Producto</vs-th>
					<vs-th >Cantidad</vs-th>
					<vs-th >Fecha</vs-th>
					<vs-th >Total</vs-th>
					<vs-th >Acciones</vs-th>
				</template>

				<template slot-scope="{data}">
					<vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">
						<vs-td :data="data[indextr].node.serie">
							{{data[indextr].node.serie}}
						</vs-td>

						<vs-td :data="data[indextr].node.NombreCliente">
							{{data[indextr].node.NombreCliente}}
						</vs-td>
						<vs-td :data="data[indextr].node.nit">
							{{data[indextr].node.nit}}
						</vs-td>
						<vs-td :data="data[indextr].node.Producto.nombreProducto">
							{{data[indextr].node.Producto.nombreProducto}}
						</vs-td>
						<vs-td :data="data[indextr].node.cantidad">
							{{data[indextr].node.cantidad}}
						</vs-td>
						<vs-td :data="data[indextr].node.Fecha">
							{{data[indextr].node.Fecha}}
						</vs-td>
						<vs-td :data="data[indextr].node.total">
							{{data[indextr].node.total}}
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
				title="Agregar Venta"
				accept-text= "Guardar"
				@accept="AgregarProducto"
				:active.sync="abrirForm"
				@cancel="close"
				@close="close"
				>
				<div class="my-4">
					<small class="date-label">Fecha de Factura</small>
			        <datepicker :language="$vs.rtl ? langHe : langEn" name="end-date" v-model="fecha"></datepicker>
				</div>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Serie" v-model="serie"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Cliente" v-model="cliente"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="NIT" v-model="NIT"></vs-input>
				<small>Producto</small>
					<v-select label="nombre" :options="listadoProductos" v-model="producto_id" :dir="$vs.rtl ? 'rtl' : 'ltr'" />
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Cantidad" v-model="cantidad"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Total" v-model="total"></vs-input>
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
				<div class="my-4">
					<small class="date-label">Fecha de Factura</small>
			        <datepicker :language="$vs.rtl ? langHe : langEn" name="end-date" v-model="fechaT"></datepicker>
				</div>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Serie" v-model="serieT"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Cliente" v-model="clienteT"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="NIT" v-model="NITT"></vs-input>
				<small>Producto</small>
					<v-select label="nombre" :options="listadoProductos" v-model="producto_idT" :dir="$vs.rtl ? 'rtl' : 'ltr'" />
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Cantidad" v-model="cantidadT"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Total" v-model="totalT"></vs-input>
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
			arrayData: [],
			listadoProductos:[],
			abrirForm:false,
			abrirEditar:false,
			langHe: es,
			langEn: es,
			endDate: '',
			startDate: '',
			id: 0,
			serie: "",
			NIT:"",
			producto_id:null,
			cantidad:0,
			fecha:"",
			total:0,
			cliente:"",
			producto_idT:null,
			idT: 0,
			serieT: "",
			NITT:"",
			producto_idT:{default: 0},
			cantidadT:0,
			fechaT:"",
			totalT:0,
			clienteT:"",
			editaID:null,
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
				valor.nombre=valor.node.nombreProducto
			}); 
			return tabla
		},
		getDate(datetime) {
			let date = new Date(datetime);
			let dateString = `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`;
			return dateString;
		},
		async AgregarProducto(){
			try {
				var result = await axios({
					method: 'POST',
					url: 'https://publicacionfinal.herokuapp.com/graphql/',
					data: {
						query:`
							mutation{
								createFactura(input:{
									NombreCliente:"${this.cliente}",
									nombreProducto:"${this.producto_id.nombre}",
									serie:${this.serie},
									nit:"${this.NIT}",
									cantidad:${this.cantidad},
									Fecha:"${this.getDate(this.fecha)}",
									total:${this.total}
								}){
									Factura{
									id
									NombreCliente
									Producto{
										id
										nombreProducto
									}
									serie
									nit
									cantidad
									Fecha
									total
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
		async EditarProducto(){
			try {
				var result = await axios({
					method: 'POST',
					url: 'https://publicacionfinal.herokuapp.com/graphql/',
					data: {
						query:`
						mutation{
							updateFactura(input:{
								id: "${this.editaID}",
								NombreCliente:"${this.clienteT}",
								nombreProducto:"${this.producto_idT.nombre}",
								serie:${this.serieT},
								nit:"${this.NITT}",
								cantidad:${this.cantidadT},
								Fecha:"${this.getDate(this.fechaT)}",
								total:${this.totalT}
							}){
								Factura{
								id
								NombreCliente
								Producto{
									id
									nombreProducto
								}
								serie
								nit
								cantidad
								Fecha
								total
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
		Editar(dato){
			let elementoE = ''
			let encontrado = false
			this.listadoProductos.forEach(function(elemento, indice, array) {
				if (elemento.node.nombreProducto==dato.Producto.nombreProducto)
					{
						elementoE=elemento
						encontrado=true
					}
				})
			this.producto_idT = encontrado == true ? elementoE:{id:dato.Producto,nombre:'No Existe'} 
			this.idT= dato.id,
			this.serieT= dato.serie,
			this.NITT=dato.nit,
			this.cantidadT=dato.cantidad,
			this.fechaT=new Date(dato.Fecha),
			this.totalT=dato.total,
			this.clienteT=dato.NombreCliente
			this.abrirEditar=true

			this.editaID=dato.id
			console.log('id de factura')
			console.log(this.editaID)
		},
		Eliminar(id){
			this.deleteId=id;
			let titulo = '';
			let color = '';

			this.$vs.dialog({
				type:'confirm',
				color: 'danger',
				title: 'Eliminar Factura',
				text: '¿Está seguro de eliminar la factura?',
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
							deleteFactura(input:{
								id: "${this.deleteId}",
							}){
								Factura{
								id
								NombreCliente
								Producto{
									id
									nombreProducto
								}
								serie
								nit
								cantidad
								Fecha
								total
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
							allFacturas{
								edges{
								node{
										NombreCliente,
								Producto{
									id,
									nombreProducto
								},
									serie,
									nit, 
									cantidad,
									Fecha,
									total,
									id,
								}
								}
							}
							}
							`
							}
						})
						// this.arrayData = result.data.data.todosProveedores
						this.arrayData = result.data.data.allFacturas.edges
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
							allProductos{
							edges{
								node{
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
						this.listadoProductos = this.traerNombre(result.data.data.allProductos.edges)
					} catch (error) {
						console.error(error)
			}
		}
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

