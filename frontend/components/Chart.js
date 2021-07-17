import { Box } from "@chakra-ui/react";
import React from "react";
import { Radar } from "react-chartjs-2";

const data = {
  labels: [
    "Integration",
    "Derivatives",
    "Conics",
    "Proofs",
    "Complex Numbers",
    "Coordinate Geometry",
  ],
  datasets: [
    {
      label: "Your Performance",
      data: [2, 6, 4, 5, 8, 6],
      backgroundColor: "rgba(255, 99, 132, 0.2)",
      borderColor: "rgba(255, 99, 132, 1)",
      borderWidth: 1,
    },
  ],
};

const options = {
  scale: {
    ticks: { beginAtZero: true },
    suggestedMax: 10,
  },
};

function Chart() {
  return (
    <Box w={500}>
      <Radar data={data} options={options} width={500} height={500} />
    </Box>
  );
}

export default Chart;
