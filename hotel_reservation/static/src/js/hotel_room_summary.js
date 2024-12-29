/** @odoo-module */

import { registry } from "@web/core/registry";
import { TextField } from "@web/views/fields/text/text_field";
import { Component, useState, onMounted } from "@odoo/owl";
import { jsonrpc } from "@web/core/network/rpc_service";

export class RoomReservation extends TextField {
    static template = 'RoomSummary'
    setup(){
        super.setup();
        this.state = useState({
            'summary_header': eval(this.props.record.data['summary_header']),
            'room_summary': eval(this.props.record.data['room_summary'])
        });
        onMounted(async () => {
            $('.o_input.cursor-pointer').on('focus',(ev) => this.onChangeDate(ev))
        })
    }
    async onChangeDate(ev){
        console.log($(ev.target).attr('data-field'))
        let response = await jsonrpc('/get-reservations', {
            date_from: $(ev.target).attr('data-field') == "date_from" ? ev.target.value :  $('input[data-field="date_from"]').val(),
            date_to: $(ev.target).attr('data-field') == "date_to" ? ev.target.value : $('input[data-field="date_to"]').val()
        })
        if (response['summary_header'] && response['room_summary']){
            this.state.summary_header = eval(response.summary_header)
            this.state.room_summary = eval(response.room_summary)
        }
    }
    get_value() {
        return this.props.record.data[this.props.name];
    }
}


export const RoomReservationProps = {
    component: RoomReservation
};

registry.category("fields").add("Room_Reservation", RoomReservationProps);
