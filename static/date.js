const in_date_time_begin_wish = document.getElementByID(in_date_time_begin_wish)
const in_date_time_end_wish = document.getElementByID(in_date_time_end_wish)

in_date_time_begin_wish.addEventListener('change', function(){
    in_date_time_end_wish.min = in_date_time_begin_wish

    date = new Date(in_date_time_begin_wish.value)
    date.SetDate(date.getDate() + 15)

    in_date_time_end_wish.max = date.toISOString().substring(0, 10)
})