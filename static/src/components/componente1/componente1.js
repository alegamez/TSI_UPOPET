/** @odoo-module **/
import { registry } from '@web/core/registry';
const { Component, useState, onWillStart, useRef } = owl;
import { useService } from "@web/core/utils/hooks";

class componente1 extends Component {
    setup() {
        this.state = useState({
            task:{name:"", descripcion:""},
            taskList:[],
            isEdit: false,
            activeId: false,
        })
        this.orm = useService("orm")
        this.model = "upopet.categoriapregunta"
        this.searchInput = useRef("search-input")

        onWillStart(async ()=>{
            await this.getAllTasks()
        })
    }

    async getAllTasks(){
        this.state.taskList = await this.orm.searchRead(this.model, [], ["name", "descripcion"])
    }

    async saveTask(){

        if (!this.state.isEdit){
            await this.orm.create(this.model, [this.state.task])
            this.resetForm()
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.task)
        }

        await this.getAllTasks()
    }

    resetForm(){
        this.state.task = {name:"", descripcion:""}
    }

    addTask(){
        this.resetForm()
        this.state.activeId = false
        this.state.isEdit = false
    }

    editTask(task){
        this.state.activeId = task.id
        this.state.isEdit = true
        this.state.task = {...task}
    }

    async deleteTask(task){
        await this.orm.unlink(this.model, [task.id])
        await this.getAllTasks()
    }

    async searchTasks(){
        const text = this.searchInput.el.value
        this.state.taskList = await this.orm.searchRead(this.model,[['name','ilike',text]], ["name", "descripcion"])
    }
       
    async updateDescripcion(e, task){
        await this.orm.write(this.model, [task.id], {descripcion: e.target.value})
        await this.getAllTasks()
    }   
 
}

componente1.template = 'owl.componente1';
registry.category('actions').add('owl.action_componente1_js', componente1);
