//DEFINICION DE VARIABLES

const url_get_products = "http://127.0.0.1:5000/api/products"
const delete_product = "http://127.0.0.1:5000/api/products"
const add_product = "http://127.0.0.1:5000/api/products"
const update_product = "http://127.0.0.1:5000/api/products"
const contenedor = document.querySelector('tbody')
let resultados = ''

const modalArticulo = new bootstrap.Modal(document.getElementById('modalArticulo'))
const formArticulo = document.querySelector('form')
const name = document.getElementById('name')
const sellin = document.getElementById('sellin')
const quality = document.getElementById('quality')
const type = document.getElementById('type')
let opcion = ''

btnCrear.addEventListener('click', ()=>{
    name.value = ''
    sellin.value = ''
    quality.value = ''
    type.value = ''
    modalArticulo.show()
    opcion = 'crear'
})

//funcion para mostrar los resultados
const mostrar = (articulos) => {
    articulos.forEach(articulo => {
            resultados += `
                <tr>
                    <td>${articulo.id}</td>
                    <td>${articulo.name}</td>
                    <td>${articulo.sellin}</td>
                    <td>${articulo.quality}</td>
                    <td>${articulo.type}</td>
                    <td class="text-center"><a class="btnEditar btn btn-primary">Update</a><a class="btnBorrar btn btn-danger">Delete</a></td>
                </tr>
    `
    })
    console.log(resultados)
    contenedor.innerHTML = resultados

}

//Procedimiento Mostrar
fetch(url_get_products)
    .then(response => response.json())
    .then(data => mostrar(data))
    .catch(error => console.log(error))

const on = (element, event, selector, handler) => {
    element.addEventListener(event, e =>{
        if (e.target.closest(selector)){
            handler(e)
        }
    })
}

//Procedimiento borrar
on(document, 'click', '.btnBorrar', e => {
    const fila = e.target.parentNode.parentNode
    const id = fila.firstElementChild.innerHTML
    alertify.confirm("This is a confirm dialog.",
    function(){
       fetch(delete_product + "/" + id,{
           method: 'DELETE'
       })
       .then(res => res.json() )
       .then( ()=> location.reload())
      },
      function(){
        alertify.error('Cancel');
  })
})


//Procedimiento editar
let idForm = 0
on(document, 'click', '.btnEditar', e => {
    const fila = e.target.parentNode.parentNode
    idForm = fila.children[0].innerHTML
    const nameForm = fila.children[1].innerHTML
    const sellinForm = fila.children[2].innerHTML
    const qualityForm = fila.children[3].innerHTML
    const typeForm = fila.children[4].innerHTML

    name.value = nameForm
    sellin.value = sellinForm
    quality.value = qualityForm
    type.value = typeForm
    opcion = 'editar'
    modalArticulo.show()
})

//procedimiento para crear y editar
formArticulo.addEventListener('submit', (e)=>{
    e.preventDefault()
    console.log(opcion)
    if (opcion === 'crear'){
        fetch(add_product, {
            method : 'POST',
            headers:  {
                'Content-Type' : 'application/json'
            },
            body: JSON.stringify({
                name:name.value,
                sellin:sellin.value,
                quality:quality.value,
                type:type.value

            })
        })
            .then (response => response.json() )
            .then (data => {
                const nuevoArticulo = []
                nuevoArticulo.push(data)
                mostrar(nuevoArticulo)
            })
    }
    if(opcion === 'editar'){
        fetch (update_product + "/" + idForm, {
            method : 'PUT',
            headers : {
                'Content-Type' : 'application/json'
            },
            body: JSON.stringify({
                name:name.value,
                sellin:sellin.value,
                quality:quality.value,
                type:type.value
            })

        })
        .then(response => response.json() )
        .then(response => location.reload())
    }
    modalArticulo.hide()
})