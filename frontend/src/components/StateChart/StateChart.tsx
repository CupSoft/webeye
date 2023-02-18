import React from 'react';
import { ResponsiveContainer, LineChart, CartesianGrid, XAxis, YAxis, Tooltip, Legend, Line } from 'recharts';
import { StateChartPropsType } from './StateChartTypes';
import styles from './StateChart.module.scss'

const data = [
  {time: '15.00',ok: 4000,partial: 2400,critical: 2400,},
  {time: '16.00',ok: 3000,partial: 1398,critical: 2210,},
  {time: '17.00',ok: 2000,partial: 9800,critical: 2290,},
  {time: '18.00',ok: 2780,partial: 3908,critical: 2000,},
  {time: '19.00',ok: 10890,partial: 4800,critical: 2181,},
  {time: '20.00',ok: 2390,partial: 3800,critical: 2500},
  {time: '21.00',ok: 3490,partial: 4300,critical: 2100,},
];

const StateChart = ({sourceUuid}: StateChartPropsType) => {
  return (
    <ResponsiveContainer 
      className={styles.chart_container}
    >
        <LineChart
          data={data}
          margin={{
            top: 10,
            right: 30,
            left: 0,
            bottom: 0,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="time" stroke='#c5c5c5'/>
          <YAxis stroke='#c5c5c5'/>
          <Tooltip wrapperClassName={styles.chart_tooltip}/>
          <Legend />
          <Line type="linear" dataKey="ok" stroke="#00ff00" fill="#00ff00" />
          <Line type="linear" dataKey="partial" stroke="#ffff00" fill="#ffff00" />
          <Line type="linear" dataKey="critical" stroke="#ff0000" fill="#ff0000" />
        </LineChart>
      </ResponsiveContainer>
  );
};

export default StateChart;