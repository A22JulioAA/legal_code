import { Calendar } from '@fullcalendar/core';
import interactionPlugin from '@fullcalendar/interaction';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';
import listPlugin from '@fullcalendar/list';

import '../styles/calendar.css'

document.addEventListener('DOMContentLoaded', function () {
    let calendarEl = document.getElementById('calendar');

    fetch('http://127.0.0.1:8000/obtener-citas').then((response) => response.json()).then((data) = < console.log(data);)

let calendar = new Calendar(calendarEl, {
    locale: 'es',
    firstDay: 1,
    titleFormat: { year: 'numeric', month: 'long' },
    plugins: [interactionPlugin, dayGridPlugin, timeGridPlugin, listPlugin],
    headerToolbar: {
        left: 'prev,next today',
        center: 'title',
        right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek'
    },
    buttonText: {
        prev: 'Anterior',
        next: 'Siguiente',
        today: 'Hoy',
        dayGridMonth: 'Mes',
        timeGridWeek: 'Semana',
        timeGridDay: 'Día',
        listWeek: 'Lista'
    },
    navLinks: true,
    editable: true,
    dayMaxEvents: true,
    events: citas

});

calendar.render();
});
