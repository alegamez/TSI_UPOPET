/** @odoo-module **/    

import { registry } from '@web/core/registry';
const { Component, useState, onWillStart, useRef } = owl;
import { useService } from "@web/core/utils/hooks";

class EspecieComponent extends Component {
    setup() {
        this.state = useState({
            especie: { nombre: "", tamanyo: 0, peso: 0, estado: "permitido", nombreCientifico: "", tipoespecie_id: 0 },
            especieList: [],
            isEdit: false,
            activeId: false,
        });
        this.orm = useService("orm");
        this.model = "upopet.especie";
        this.searchInput = useRef("search-input");

        onWillStart(async () => {
            await this.getAllEspecies();
        });
    }

    async getAllEspecies() {
        this.state.especieList = await this.orm.searchRead(this.model, [], ["nombre", "tamanyo", "peso", "estado", "nombreCientifico", "tipoespecie_id"]);
    }

    addEspecie() {
        this.resetForm();
        this.state.activeId = false;
        this.state.isEdit = false;
    }

    editEspecie(especie) {
        this.state.activeId = especie.id;
        this.state.isEdit = true;
        this.state.especie = { ...especie };
    }

    async saveEspecie() {
        if (!this.state.isEdit) {
            await this.orm.create(this.model, [this.state.especie]);
            this.resetForm();
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.especie);
        }
        $('#especieModal').modal('hide');
        this.resetForm();
        await this.getAllEspecies();
    }

    resetForm() {
        this.state.especie = { nombre: "", tamanyo: 0, peso: 0, estado: "permitido", nombreCientifico: "", tipoespecie_id: 0 };
    }

    async deleteEspecie(especie) {
        await this.orm.unlink(this.model, [especie.id]);
        await this.getAllEspecies();
    }

    async searchEspecies() {
        const text = this.searchInput.el.value;
        this.state.especieList = await this.orm.searchRead(this.model, [['nombre', 'ilike', text]], ["nombre", "tamanyo", "peso", "estado", "nombreCientifico", "tipoespecie_id"]);
    }
}
    
EspecieComponent.template = 'owl.EspecieComponent';
registry.category('actions').add('owl.action_EspecieComponent_js', EspecieComponent);
