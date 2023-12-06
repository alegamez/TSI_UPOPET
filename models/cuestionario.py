<odoo>
    <!-- tree view -->
    <record id="view_cuestionario_tree" model="ir.ui.view">
        <field name="name">cuestionario.tree</field>
        <field name="model">upopet.cuestionario</field>
        <field name="arch" type="xml">
            <tree string="Cuestionario">
                <field name="name"/>
                <field name="jardin"/>
                <field name="espacioDisponible"/>
                <field name="experienciaPrevia"/>
                <field name="exotico"/>
                <field name="preferencia"/>
                <field name="usuario_id"/>
            </tree>
        </field>
    </record>

    <!-- form view -->
    <record id="view_cuestionario_form" model="ir.ui.view">
        <field name="name">cuestionario.form</field>
        <field name="model">upopet.cuestionario</field>
        <field name="arch" type="xml">
            <form string="Cuestionario">
                <sheet>
                    <group>
                        <field name="name"/>
                        <field name="jardin"/>
                        <field name="espacioDisponible"/>
                        <field name="experienciaPrevia"/>
                        <field name="exotico"/>
                        <field name="preferencia"/>
                        <field name="usuario_id"/>
                    </group>
                </sheet>
            </form>
        </field>
    </record>

    <!-- action to open the tree & form view -->
    <record id="cuestionario_list_action" model="ir.actions.act_window">
        <field name="name">Cuestionario</field>
        <field name="res_model">upopet.cuestionario</field>
        <field name="view_mode">tree,form</field>
    </record>

</odoo>
