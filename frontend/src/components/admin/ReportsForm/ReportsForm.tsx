import React, { useEffect, useState } from 'react';
import { useAdminDeleteReportMutation, useAdminPatchReportMutation, useGetAllReportsQuery } from '../../../services/apiService/apiService';
import { ReportResponseTypes } from '../../../services/apiService/apiServiceTypes';
import ReportBadge from '../../ReportBadge/ReportBadge';

const ReportsForm = () => {
  let {data, isLoading} = useGetAllReportsQuery()
  const [reports, setReports] = useState<ReportResponseTypes[]>()
  const [adminDeleteReport] = useAdminDeleteReportMutation()
  const [adminPatchReport] = useAdminPatchReportMutation()

  useEffect(() => {
    if (data) {
      setReports(data)
    }
  }, [data])

  if (isLoading) {
    return null
  }

  function deleteClickHandler(evt: React.MouseEvent, uuid: string) {
    adminDeleteReport(uuid).then(value => {
      if ('error' in value) {
        return
      }

      setReports(reports?.filter((report) => report.uuid !== uuid))
    })
  }

  async function patchClickHandler(evt: React.MouseEvent, uuid: string) {
    const value = await adminPatchReport({uuid, is_moderated: true})

    if ('error' in value) {
      return
    }

    setReports(reports?.filter((report) => report.uuid !== uuid))
  }

  return (
    <div className='admin_container'>
      <div className='admin_wrapper'>
        <h3 className='admin_title'>Заявки о доступности ресурсов</h3>
          {reports && [...reports].sort((a, b) => a.resource_name >= b.resource_name ? 1 : -1).map(report =>
            <ReportBadge 
              deleteClickHandler={(evt) => deleteClickHandler(evt, report.uuid)}
              showModerated={false}
              pacthClickHandler={(evt) => patchClickHandler(evt, report.uuid)}
              key={report.uuid} 
              {...report}
            />
          )}
      </div>
    </div>
  );
};

export default ReportsForm;