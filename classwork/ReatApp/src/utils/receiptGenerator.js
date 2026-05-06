export const generateReceipt = (student, installment) => {
  const receiptWindow = window.open('', '_blank');
  
  const html = `
    <!DOCTYPE html>
    <html>
    <head>
      <title>Payment Receipt - ${student.name}</title>
      <style>
        body { font-family: 'Inter', sans-serif; padding: 40px; color: #1a1a1a; line-height: 1.6; }
        .receipt-container { max-width: 800px; margin: 0 auto; border: 2px solid #f0f0f0; padding: 40px; border-radius: 20px; position: relative; overflow: hidden; }
        .watermark { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%) rotate(-45deg); font-size: 100px; color: rgba(0,0,0,0.03); font-weight: 800; z-index: -1; white-space: nowrap; }
        .header { display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 2px solid #6366f1; padding-bottom: 20px; margin-bottom: 30px; }
        .logo-section h1 { margin: 0; color: #6366f1; font-size: 28px; font-weight: 800; }
        .logo-section p { margin: 5px 0 0 0; color: #666; font-size: 12px; }
        .receipt-info { text-align: right; }
        .receipt-info h2 { margin: 0; color: #1a1a1a; font-size: 24px; text-transform: uppercase; }
        .receipt-info p { margin: 5px 0; color: #666; font-size: 14px; }
        
        .details-grid { display: grid; grid-template-cols: 1fr 1fr; gap: 30px; margin-bottom: 40px; }
        .detail-box h4 { margin: 0 0 10px 0; color: #6366f1; text-transform: uppercase; font-size: 12px; letter-spacing: 1px; }
        .detail-box p { margin: 0; font-size: 16px; font-weight: 600; }
        
        .payment-table { width: 100%; border-collapse: collapse; margin-bottom: 40px; }
        .payment-table th { background: #f8fafc; padding: 15px; text-align: left; border-bottom: 2px solid #e2e8f0; font-size: 12px; text-transform: uppercase; color: #64748b; }
        .payment-table td { padding: 15px; border-bottom: 1px solid #f1f5f9; font-size: 15px; }
        
        .summary-section { display: flex; justify-content: flex-end; }
        .summary-box { width: 250px; background: #f8fafc; padding: 20px; border-radius: 15px; }
        .summary-row { display: flex; justify-content: space-between; margin-bottom: 10px; }
        .summary-row.total { border-top: 2px solid #e2e8f0; padding-top: 10px; margin-top: 10px; font-weight: 800; color: #6366f1; font-size: 18px; }
        .summary-row span:first-child { color: #64748b; font-size: 13px; }
        
        .footer { margin-top: 60px; display: flex; justify-content: space-between; align-items: flex-end; }
        .signature { border-top: 1px solid #ccc; width: 200px; text-align: center; padding-top: 10px; font-size: 12px; color: #666; }
        .thanks { color: #6366f1; font-weight: 600; font-style: italic; }
        
        @media print {
          .no-print { display: none; }
          body { padding: 0; }
          .receipt-container { border: none; }
        }
        .print-btn { background: #6366f1; color: white; border: none; padding: 12px 25px; border-radius: 10px; font-weight: 600; cursor: pointer; margin-bottom: 20px; display: inline-flex; align-items: center; gap: 8px; }
      </style>
    </head>
    <body>
      <div class="no-print" style="text-align: center;">
        <button class="print-btn" onclick="window.print()">Print Receipt / Save as PDF</button>
      </div>
      
      <div class="receipt-container">
        <div class="watermark">ENJOY PREMIUM</div>
        
        <div class="header">
          <div class="logo-section">
            <h1>Enjoy Premium</h1>
            <p>Coaching Institute Management System</p>
          </div>
          <div class="receipt-info">
            <h2>Receipt</h2>
            <p>No: #RCP-${installment.id}-${new Date().getFullYear()}</p>
            <p>Date: ${installment.payment_date}</p>
          </div>
        </div>

        <div class="details-grid">
          <div class="detail-box">
            <h4>Billed To:</h4>
            <p>${student.name}</p>
            <p style="font-weight: 400; font-size: 13px; color: #666;">${student.email}</p>
            <p style="font-weight: 400; font-size: 13px; color: #666;">Contact: ${student.mobile || 'N/A'}</p>
          </div>
          <div class="detail-box">
            <h4>Course Details:</h4>
            <p>${student.course_name}</p>
            <p style="font-weight: 400; font-size: 13px; color: #666;">Enrollment Date: ${student.joined_date}</p>
          </div>
        </div>

        <table class="payment-table">
          <thead>
            <tr>
              <th>Description</th>
              <th>Payment Date</th>
              <th>Remarks</th>
              <th style="text-align: right;">Amount</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Course Fee Installment</td>
              <td>${installment.payment_date}</td>
              <td>${installment.remarks || 'Standard Payment'}</td>
              <td style="text-align: right; font-weight: 700;">₹${installment.amount}</td>
            </tr>
          </tbody>
        </table>

        <div class="summary-section">
          <div class="summary-box">
            <div class="summary-row">
              <span>Total Course Fee</span>
              <span>₹${student.total_fees}</span>
            </div>
            <div class="summary-row">
              <span>Total Paid Before</span>
              <span>₹${student.fees_paid - installment.amount}</span>
            </div>
            <div class="summary-row total">
              <span>Amount Paid</span>
              <span>₹${installment.amount}</span>
            </div>
            <div class="summary-row" style="margin-top: 15px; font-weight: 600; color: #ef4444;">
              <span>Balance Remaining</span>
              <span>₹${student.total_fees - student.fees_paid}</span>
            </div>
          </div>
        </div>

        <div class="footer">
          <div>
            <p class="thanks">Thank you for choosing Enjoy Premium!</p>
            <p style="font-size: 10px; color: #999; margin-top: 5px;">This is a computer generated receipt.</p>
          </div>
          <div class="signature">
            Authorized Signatory
          </div>
        </div>
      </div>
    </body>
    </html>
  `;
  
  receiptWindow.document.write(html);
  receiptWindow.document.close();
};
