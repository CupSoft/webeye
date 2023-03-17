import React from 'react';
import { useGetAllReportsQuery } from '../../../services/apiService/apiService';
import ReportBadge from '../ReportBadge/ReportBadge';

const ReportsForm = () => {
  let {data: reports, isLoading} = useGetAllReportsQuery()

  if (isLoading) {
    return null
  }

  // reports = [
  //   {created_at: new Date().toString(), uuid: '1', status: 'critical', resource_name: 'HSE', is_moderated: false, text: 'Не работает сайт'},
  //   {created_at: new Date().toString(), uuid: '2', status: 'critical', resource_name: 'ABC', is_moderated: false, text: 'Плохо работает сайт'},
  // ]

  return (
    <div className='admin_container'>
      <div className='admin_wrapper'>
        <h3 className='admin_title'>Заявки о доступности ресурсов</h3>
          {reports && [...reports].sort((a, b) => a.resource_name >= b.resource_name ? 1 : -1).map(report =>
            <ReportBadge key={report.uuid} {...report}/>
          )}
      </div>
    </div>
  );
};

export default ReportsForm;