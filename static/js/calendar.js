import { Calendar } from '/node_modules/@fullcalendar/core'
import dayGridPlugin from '/@fullcalendar/daygrid'
const calendar = new Calendar(container, {
    plugins: [dayGridPlugin],
    initialView: "dayGridMonth",
    headerToolbar: {
        left: "prev,next today",
        center: "title",
        right: "dayGridMonth,timeGridWeek,listWeek",
    },
    selectable: true,
    events: [
        { id: 1, title: "Event 1", start: "2023-09-05", end: "2023-09-10" },
        { id: 2, title: "Event 2", start: "2023-09-12", end: "2023-09-14" }],
    eventClick: (eventInfo) => { console.log('Click on Event') },
    select: (dateRange) => { console.log("Selected date range in calendar") },
});

calendar.render();