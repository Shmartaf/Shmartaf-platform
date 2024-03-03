import { Button, Typography, Card } from "@mui/material";
import Box from "@mui/material/Box";
import { DataGrid } from "@mui/x-data-grid";
import { Link } from "react-router-dom";
import FiberManualRecordIcon from "@mui/icons-material/FiberManualRecord";

const rows = [
  {
    id: 1,
    number: 1,
    date: "10.2.2024",
    name: "Odel Levi",
    address: "Tel Aviv, Jabotinsky 24",
    image: "https://i.pravatar.cc/30?img=1",
  },

  {
    id: 2,
    number: 2,
    date: "13.3.2024",
    name: "Razib Rahman",
    address: "Ramat Gan, Yashar 12",
    image: "https://i.pravatar.cc/30?img=2",
  },

  {
    id: 3,
    number: 3,
    date: "01.01.2024",
    name: "Luke Norton",
    address: "Haifa, Herzl 27",
    image: "https://i.pravatar.cc/30?img=3",
  },
];

const columns = [
  { field: "number", headerName: "No.", width: 60 },
  {
    field: "date",
    headerName: "Date",
    width: 120,
    renderCell: (params) => {
      return (
        <Box
          sx={{
            display: "flex",
            gap: 1,
            alignItems: "center",
            backgroundColor: "#f2f2f2",
            borderRadius: 2,
            padding: "5px 10px",
          }}>
          <Typography>{params.row.date}</Typography>
        </Box>
      );
    },
  },
  {
    field: "name",
    headerName: "Parent",
    width: 230,
    renderCell: (params) => {
      return (
        <Box sx={{ display: "flex", gap: 1, alignItems: "center" }}>
          <img
            src={params.row.image}
            style={{ width: "34px", height: "34px", borderRadius: "50%" }}
          />
          <Typography>{params.row.name}</Typography>
        </Box>
      );
    },
  },
  {
    field: "address",
    headerName: "Address",
    width: 230,
    renderCell: (params) => {
      return (
        <Box
          sx={{
            display: "flex",
            gap: 1,
            alignItems: "center",
            backgroundColor: "#f2f2f2",
            borderRadius: 2,
            padding: "5px 10px",
          }}>
          <Typography>{params.row.address}</Typography>
        </Box>
      );
    },
  },
];

const UpcomingEvents = () => {
  const actionColumn = [
    {
      field: "action",
      headerName: "",
      width: 80,
      sortable: false,
      renderCell: (params) => {
        return (
          <Box sx={{ display: "flex", gap: 2, alignItems: "center" }}>
            <Button
              LinkComponent={Link}
              // to={`/orders/${params.row.id}`}
              // state={params.row}
              variant="contained"
              style={{ textDecoration: "none" }}
              size="small"
              sx={{ textTransform: "none" }}>
              Details
            </Button>
          </Box>
        );
      },
    },
  ];

  return (
    <Box
    sx={{
      display: "flex",
      flexDirection: "column",
      gap: "10px",
      width: "100%",
      pt: 2,
      pr: 2,
      backgroundColor: "#F8F7F1",
    }}>
    <Card
      sx={{
        p: 2,
        display: "flex",
        flexDirection: "column",
        gap: 2,
        minWidth: 250,
        width: "100%",
        borderRadius: 2,
        boxShadow: 2,
      }}>
      <Box
        width={"100%"}
        sx={{ display: "flex", justifyContent: "flex-start" }}>
        <Typography variant="h6">Upcoming Events</Typography>
      </Box>
      <DataGrid
        rows={rows}
        columns={columns.concat(actionColumn)}
        initialState={{
          pagination: {
            paginationModel: { page: 0, pageSize: 50 },
          },
          sorting: {
            sortModel: [{ field: "date", sort: "desc" }],
          },
        }}
        pageSizeOptions={[10, 20, 50, 100]}
        // checkboxSelection
        // onRowClick={(params) => { navigate(`/orders/${params.row.id}`) }}
      />
    </Card>
    </Box>
  );
};
export default UpcomingEvents;
