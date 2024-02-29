import { Typography } from "@mui/material";
import Box from "@mui/material/Box";
import StarIcon from "@mui/icons-material/Star";

const NotificationCard = (props) => {
  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        gap: 1,
        width: "100%",
        height: "140px",
        justifyContent: "start",
        alignItems: "center",
        padding: "10px",
        boxShadow: 2,
        borderRadius: 2,
      }}
    >

      <Typography variant="h6" fontWeight={"bold"}>
        {props.name}
      </Typography>
      <Typography variant="h6" fontWeight={"bold"}>
        {props.location} {props.date}
      </Typography>
      <Box
        sx={{
          display: "flex",
          flexDirection: "row",
          gap: 1,
          alignItems: "center",
          justifyContent: "center",
          padding: "5px 5px",
        }}
      >
        <Typography>{props.desc}</Typography>
      </Box>
    </Box>
  );
};
export default NotificationCard;
