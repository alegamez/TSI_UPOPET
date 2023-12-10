/** @odoo-module **/
import { registry } from '@web/core/registry';
const { Component, useState, onWillStart, useRef } = owl;
import { useService } from "@web/core/utils/hooks";

class empresaComponente extends Component {
    setup() {
        this.state = useState({
            task:{name:"", nombreEmpresa:""},
            taskList:[],
            isEdit: false,
            activeId: false,
        })
        this.orm = useService("orm")
        this.model = "upopet.empresa"
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
        this.state.task = {name:"", nombreEmpresa:""}
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
        this.state.taskList = await this.orm.searchRead(this.model,[['name','ilike',text]], ["name", "nombreEmpresa"])
    }
       
    async updateNombreEmpresa(e, task){
        await this.orm.write(this.model, [task.id], {nombreEmpresa: e.target.value})
        await this.getAllTasks()
    }   
 
}

empresaComponente.template = 'owl.empresaComponente';
registry.category('actions').add('owl.action_empresaComponente_js', empresaComponente);
