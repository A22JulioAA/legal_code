import { Calendar } from '@fullcalendar/core';
import interactionPlugin from '@fullcalendar/interaction';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';
import listPlugin from '@fullcalendar/list';

document.addEventListener('DOMContentLoaded', function () {
    let calendarEl = document.getElementById('calendar');

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
        // events: citas

    });

    calendar.render();
});
