import React, { useState, useEffect } from 'react';
import { 
  Calendar, 
  Phone, 
  Users, 
  AlertCircle, 
  CheckCircle, 
  Clock, 
  LayoutDashboard, 
  PhoneCall,
  Activity,
  UserPlus
} from 'lucide-react';

const App = () => {
  // Veri Durumları (State)
  const [appointments, setAppointments] = useState([]);
  const [callLogs, setCallLogs] = useState([]);
  const [stats, setStats] = useState({
    totalCalls: 0,
    newAppointments: 0,
    urgentTransfers: 0
  });
  const [isLoading, setIsLoading] = useState(true);

  // Verileri API'den Çekme (Simulation)
  useEffect(() => {
    const fetchData = async () => {
      try {
        // Not: Gerçek senaryoda burası "http://localhost:8000/api/dashboard" adresine istek atacak
        // Şimdilik mock veri ile dolduruyoruz
        setTimeout(() => {
          setAppointments([
            { id: 1, patient: "Ahmet Yılmaz", time: "10:30", type: "Kanal Tedavisi", status: "Onaylandı" },
            { id: 2, patient: "Ayşe Demir", time: "11:45", type: "Genel Kontrol", status: "Beklemede" },
            { id: 3, patient: "Mehmet Can", time: "14:15", type: "Dolgu", status: "İptal" },
          ]);
          setCallLogs([
            { id: 101, patient: "Bilinmeyen", phone: "0505...", sentiment: "Acil", transcript: "Ağrım çok şiddetli...", status: "Aktarıldı" },
            { id: 102, patient: "Zeynep Kaya", phone: "0555...", sentiment: "Pozitif", transcript: "Randevu teyidi için aramıştım.", status: "AI Çözdü" },
          ]);
          setStats({ totalCalls: 42, newAppointments: 18, urgentTransfers: 4 });
          setIsLoading(false);
        }, 800);
      } catch (error) {
        console.error("Veri çekme hatası:", error);
        setIsLoading(false);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="flex h-screen bg-slate-50 font-sans text-slate-900">
      {/* SIDEBAR */}
      <aside className="w-64 bg-slate-900 text-white flex flex-col shadow-xl">
        <div className="p-6 flex items-center gap-3">
          <div className="bg-blue-500 p-2 rounded-lg shadow-lg shadow-blue-500/20">
            <Calendar className="text-white" size={20} />
          </div>
          <span className="text-xl font-bold tracking-tight">Dişçi AI</span>
        </div>
        
        <nav className="flex-1 px-4 space-y-2 mt-4">
          <NavItem icon={<LayoutDashboard size={18}/>} label="Dashboard" active />
          <NavItem icon={<Calendar size={18}/>} label="Randevular" />
          <NavItem icon={<PhoneCall size={18}/>} label="Arama Kayıtları" />
          <NavItem icon={<Users size={18}/>} label="Hastalar" />
          <NavItem icon={<Activity size={18}/>} label="AI Analizleri" />
        </nav>

        <div className="p-4 border-t border-slate-800">
          <div className="bg-slate-800 rounded-xl p-4 flex items-center gap-3">
            <div className="w-10 h-10 rounded-full bg-blue-500 flex items-center justify-center font-bold">DR</div>
            <div>
              <p className="text-sm font-bold">Dr. Klinik</p>
              <p className="text-xs text-slate-400">Yönetici</p>
            </div>
          </div>
        </div>
      </aside>

      {/* MAIN CONTENT */}
      <main className="flex-1 overflow-y-auto p-8">
        <header className="flex justify-between items-center mb-10">
          <div>
            <h1 className="text-3xl font-extrabold tracking-tight">Klinik Durumu</h1>
            <p className="text-slate-500 mt-1">AI asistanınız şu an aktif ve aramaları karşılıyor.</p>
          </div>
          <button className="flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white px-5 py-2.5 rounded-xl font-semibold shadow-lg shadow-blue-600/20 transition-all">
            <UserPlus size={18} />
            <span>Yeni Kayıt</span>
          </button>
        </header>

        {/* ISTATISTIK KARTLARI */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
          <StatBox 
            title="Toplam Arama" 
            value={stats.totalCalls} 
            icon={<Phone size={24}/>} 
            color="blue" 
            trend="+%12"
          />
          <StatBox 
            title="Yeni Randevular" 
            value={stats.newAppointments} 
            icon={<CheckCircle size={24}/>} 
            color="emerald" 
            trend="+5 bugün"
          />
          <StatBox 
            title="Acil Yönlendirme" 
            value={stats.urgentTransfers} 
            icon={<AlertCircle size={24}/>} 
            color="rose" 
            trend="Önemli"
          />
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* RANDEVU TABLOSU */}
          <div className="lg:col-span-2 bg-white rounded-3xl shadow-sm border border-slate-100 overflow-hidden">
            <div className="p-6 border-b border-slate-50 flex justify-between items-center">
              <h2 className="text-xl font-bold">Günlük Takvim</h2>
              <button className="text-blue-600 text-sm font-semibold hover:text-blue-700">Tümünü Gör</button>
            </div>
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead className="bg-slate-50 text-slate-500 text-xs uppercase tracking-wider font-bold">
                  <tr>
                    <th className="px-6 py-4 text-left">Hasta</th>
                    <th className="px-6 py-4 text-left">İşlem</th>
                    <th className="px-6 py-4 text-left">Saat</th>
                    <th className="px-6 py-4 text-left">Durum</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-50">
                  {appointments.map((apt) => (
                    <tr key={apt.id} className="hover:bg-slate-50/50 transition-colors">
                      <td className="px-6 py-4 font-bold text-slate-700">{apt.patient}</td>
                      <td className="px-6 py-4 text-slate-600 text-sm">{apt.type}</td>
                      <td className="px-6 py-4 text-slate-500 text-sm">{apt.time}</td>
                      <td className="px-6 py-4">
                        <StatusBadge status={apt.status} />
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          {/* CANLI AI AKTIVITESI */}
          <div className="bg-white rounded-3xl shadow-sm border border-slate-100 p-6">
            <div className="flex items-center gap-2 mb-6">
              <div className="w-2 h-2 rounded-full bg-red-500 animate-pulse"></div>
              <h2 className="text-xl font-bold text-slate-800">Canlı AI Akışı</h2>
            </div>
            <div className="space-y-6">
              {callLogs.map((call) => (
                <div key={call.id} className="group cursor-pointer">
                  <div className="flex justify-between items-center mb-2">
                    <span className="text-[10px] font-bold uppercase tracking-widest text-slate-400">Yeni Arama</span>
                    <span className={`text-[10px] font-black px-2 py-0.5 rounded-md ${
                      call.sentiment === 'Acil' ? 'bg-rose-100 text-rose-600' : 'bg-emerald-100 text-emerald-600'
                    }`}>
                      {call.sentiment}
                    </span>
                  </div>
                  <h3 className="text-sm font-bold text-slate-800 group-hover:text-blue-600 transition-colors">{call.status}</h3>
                  <p className="text-xs text-slate-500 mt-1 line-clamp-2 leading-relaxed italic">"{call.transcript}"</p>
                  <div className="mt-3 h-px bg-slate-50"></div>
                </div>
              ))}
            </div>
            <button className="w-full mt-8 py-3 bg-slate-50 hover:bg-slate-100 text-slate-500 rounded-2xl text-xs font-bold transition-colors">
              Tüm Görüşme Kayıtları
            </button>
          </div>
        </div>
      </main>
    </div>
  );
};

// YARDIMCI BILEŞENLER
const NavItem = ({ icon, label, active = false }) => (
  <button className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition-all ${
    active ? 'bg-blue-600 text-white shadow-lg shadow-blue-600/20' : 'text-slate-400 hover:text-white hover:bg-slate-800'
  }`}>
    {icon}
    <span className="text-sm font-semibold">{label}</span>
  </button>
);

const StatBox = ({ title, value, icon, color, trend }) => {
  const colorMap = {
    blue: "bg-blue-50 text-blue-600 border-blue-100",
    emerald: "bg-emerald-50 text-emerald-600 border-emerald-100",
    rose: "bg-rose-50 text-rose-600 border-rose-100"
  };
  return (
    <div className={`p-6 rounded-[2rem] border bg-white shadow-sm flex items-center gap-5 transition-transform hover:scale-[1.02]`}>
      <div className={`p-4 rounded-2xl ${colorMap[color].split(' ')[0]} ${colorMap[color].split(' ')[1]}`}>
        {icon}
      </div>
      <div>
        <p className="text-slate-400 text-xs font-bold uppercase tracking-wider">{title}</p>
        <div className="flex items-center gap-2">
          <span className="text-2xl font-black text-slate-800">{value}</span>
          <span className={`text-[10px] font-bold ${colorMap[color].split(' ')[1]}`}>{trend}</span>
        </div>
      </div>
    </div>
  );
};

const StatusBadge = ({ status }) => {
  const colors = {
    "Onaylandı": "bg-emerald-100 text-emerald-700",
    "Beklemede": "bg-amber-100 text-amber-700",
    "İptal": "bg-slate-100 text-slate-500"
  };
  return (
    <span className={`px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-tight ${colors[status] || colors["İptal"]}`}>
      {status}
    </span>
  );
};

export default App;

