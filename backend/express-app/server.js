const express = require('express');
const cors = require('cors');
const PORT = 8080;
const app = express()

app.use(cors())
app.use(express.json())


app.post('/mark-attendance', (req, res) => {
    res.json({ message: 'Attendance marked successfully' })
})

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`)
});