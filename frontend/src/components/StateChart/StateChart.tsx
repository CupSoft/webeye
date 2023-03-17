import { useRef, useState } from 'react';
import { Bar, BarChart, CartesianGrid, Legend, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';
import { useGetAllCheckResultsQuery } from '../../services/apiService/apiService';
import { GetCheckResultsResponseTypes } from '../../services/apiService/apiServiceTypes';
import ChartLoader from '../ChartLoader/ChartLoader';
import styles from './StateChart.module.scss';
import { StateChartPropsType } from './StateChartTypes';

const StateChart = ({sourceUuid, max_count=7, timedelta=3600}: StateChartPropsType) => {
  const {data, isLoading} = useGetAllCheckResultsQuery({max_count, timedelta, source_uuid: sourceUuid});
  const [needShowTooltip, setNeedShowTooltip] = useState(!('ontouchstart' in window))
  const ref = useRef(null)

  // useOnTouchOutside(ref, () => {
  //   setNeedShowTooltip(false)
  // })
  // useOnInside(ref, () => {
  //   setNeedShowTooltip(true)
  // })

  if (isLoading) {
    return <ChartLoader/>
  }

  function normalizeData(data: GetCheckResultsResponseTypes[] | undefined): GetCheckResultsResponseTypes[] {
    if (!data) {
      return []
    }

    return data.map(obj => {
      let end_datetime = ''

      const date = new Date(obj.end_datetime)
      const now = new Date()

      if (now.getDate() === date.getDate()
        && now.getMonth() === date.getMonth()
        && now.getFullYear() === date.getFullYear()) {
        end_datetime = date.toLocaleTimeString().slice(0, -3)
      } else {
        if (now.getFullYear() === date.getFullYear()) {
          const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
          end_datetime = date.getDate() + ' ' + monthNames[date.getMonth()]
        } else {
          end_datetime = date.toLocaleDateString()
        }
      }

      return {...obj, end_datetime}
    })
  }

  return (
    <ResponsiveContainer 
      className={styles.chart_container}
      ref={ref}
    >
        <BarChart
          onClick={() => {}}
          data={normalizeData(data)}
          margin={{
            top: 10,
            right: 30,
            left: 0,
            bottom: 0,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="end_datetime" stroke='#c5c5c5'/>
          <YAxis stroke='#c5c5c5'/>
          {needShowTooltip && <Tooltip wrapperClassName={styles.chart_tooltip} />}
          <Legend />
          <Bar dataKey="ok" stackId='1' fill="#0DC268" />
          <Bar dataKey="partial" stackId='1' fill="#FF9E00" />
          <Bar dataKey="critical" stackId='1' fill="#ED0A34" />
        </BarChart>
      </ResponsiveContainer>
  );
};

export default StateChart;