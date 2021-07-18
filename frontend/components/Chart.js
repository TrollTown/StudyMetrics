import { Box } from "@chakra-ui/react";
import React from "react";
import { Radar } from "react-chartjs-2";

function Chart({ message, type }) {
  let scores = [];
  let categories = [];
  if (message === "Your Performance") {
    if (type === "math")
      categories = [
        "Integration",
        "Derivatives",
        "Conics",
        "Proofs",
        "Complex Numbers",
        "Coordinate Geometry",
      ];
    else
      categories = [
        "HSC Physics",
        "HSC Maths Ext2",
        "HSC Biology",
        "HSC Economics",
        "HSC Maths Ext1",
        "HSC English Advanced",
      ];

    scores = [3, 7, 4, 2, 5, 3];
  } else {
    categories = [
      "12AMathsExtII",
      "12CAdvMath",
      "11BMath",
      "10AMath",
      "9GMath",
      "7RMath",
    ];
    scores = [4, 7, 6, 8, 5, 9];
  }
  const data = {
    labels: categories,
    datasets: [
      {
        label: message,
        data: scores,
        backgroundColor: "#D6BCFA",
        borderColor: "#805AD5",
        borderWidth: 1,
      },
    ],
  };

  const options = {
    scale: {
      ticks: { beginAtZero: true },
      suggestedMin: 0,
      suggestedMax: 10,
    },
  };
  return (
    <Box w={500}>
      <Radar data={data} options={options} width={450} height={450} />
    </Box>
  );
}

export default Chart;
