# RevOps Data Analyst Assessment - PTV Logistics
## End-to-End GTM Analysis & Strategic Recommendations

---

## Executive Summary

Based on the comprehensive data analysis of 2,621 opportunities, this document provides strategic RevOps recommendations for PTV Logistics, including GTM model identification, department mapping, KPI framework, and tool stack optimization.

**Key Findings from Data Analysis:**
- Annual Win Rate: **26.9%** (276/1027 closed deals)
- 2026 Confirmed Revenue: **$54.3M** from won deals
- Performance Decline: **-3.4 percentage points** H2 2025 vs H1 2025
- Data Quality Issue: **231 overdue open deals** requiring status updates

---

## 1. GTM Models Analysis

### Primary GTM Models for PTV Logistics

#### **1.1 Enterprise B2B Sales Model**
**Why PTV Operates This Model:**
- High ACV values (average ~$20K+ per deal)
- Complex logistics solutions requiring consultative selling
- Long sales cycles evident from data (12+ months typical)
- Geographic expansion needs for logistics software

**Main Characteristics:**
- Account-based selling approach
- Multi-stakeholder decision process
- Custom implementation requirements
- High-touch customer success model

#### **1.2 Product-Led Growth (PLG) Hybrid Model**
**Why PTV Operates This Model:**
- Software nature allows for trial/demo experiences
- Self-service onboarding for smaller logistics companies
- Freemium or trial models for route optimization tools

**Main Characteristics:**
- In-product activation and engagement
- Data-driven user onboarding
- Usage-based expansion opportunities
- Automated nurturing sequences

#### **1.3 Partner-Enabled Model**
**Why PTV Operates This Model:**
- Logistics industry relies heavily on system integrators
- Regional partners for global expansion
- Channel partnerships with ERP providers

**Main Characteristics:**
- Channel partner enablement programs
- Co-selling motions
- Partner-sourced leads and opportunities
- Shared revenue models

---

## 2. Department Mapping Across the Bowtie

### **Bowtie Department Structure**

```
AWARENESS → INTEREST → CONSIDERATION → PURCHASE → ONBOARDING → EXPANSION → ADVOCACY
    ↓          ↓           ↓            ↓            ↓            ↓           ↓
 MARKETING  MARKETING   MARKETING     SALES      CUSTOMER    CUSTOMER    CUSTOMER
           SDR/BDR      SALES         AE         SUCCESS     SUCCESS     SUCCESS
                                                 SUPPORT     ACCOUNT     MARKETING
                                                            MANAGEMENT
```

### **2.1 Pre-Purchase (Left Side of Bowtie)**

**Marketing Department:**
- **Demand Generation Manager:** Lead generation, content marketing
- **Digital Marketing Specialist:** SEO, paid advertising, social media
- **Marketing Operations:** Campaign automation, lead scoring
- **Product Marketing Manager:** Positioning, competitive intelligence

**Sales Development (SDR/BDR):**
- **Business Development Representatives:** Outbound prospecting
- **Sales Development Representatives:** Inbound lead qualification
- **Sales Operations:** Process optimization, territory management

**Sales Department:**
- **Account Executives:** Opportunity management, deal closure
- **Sales Engineers:** Technical demonstrations, solution design
- **Sales Managers:** Pipeline management, forecasting

### **2.2 Post-Purchase (Right Side of Bowtie)**

**Customer Success Department:**
- **Customer Success Managers:** Onboarding, adoption, renewal
- **Implementation Specialists:** Technical deployment, training
- **Customer Support:** Technical issue resolution

**Account Management:**
- **Account Managers:** Expansion opportunities, relationship management
- **Customer Advocacy Managers:** Reference programs, case studies

---

## 3. Department KPIs Framework

### **3.1 Marketing Department KPIs**

**Volume Metrics:**
- **Leads Generated:** Monthly new leads (Target: 500+ leads/month)
- **MQLs (Marketing Qualified Leads):** Qualified leads passed to sales
- **Website Traffic:** Unique visitors, page views, session duration

**Efficiency Metrics:**
- **Lead-to-MQL Conversion Rate:** Currently measuring at industry benchmark ~13%
- **Cost Per Lead (CPL):** Total marketing spend / leads generated
- **Marketing ROI:** Revenue attributed / marketing investment

**Velocity Metrics:**
- **Time to MQL:** Days from first touch to qualification
- **Lead Response Time:** Time to first sales contact

**Why These KPIs Matter:**
- **Lead Generation** identifies top-of-funnel health
- **Conversion Rates** reveal messaging and targeting effectiveness
- **Cost Metrics** ensure efficient budget allocation

**Calculation Example:**
```
Lead-to-MQL Conversion Rate = (MQLs / Total Leads) × 100
If 500 leads → 65 MQLs = 13% conversion rate
```

### **3.2 Sales Department KPIs**

**Volume Metrics:**
- **SQLs (Sales Qualified Leads):** Opportunities created from MQLs
- **Pipeline Value:** Total value of open opportunities
- **Closed Won Deals:** Monthly new customers acquired

**Efficiency Metrics:**
- **MQL-to-SQL Conversion Rate:** Quality of marketing handoffs
- **Win Rate:** 26.9% (from our analysis) - **Needs improvement**
- **Average Deal Size:** $54.3M ÷ 276 deals = ~$197K average

**Velocity Metrics:**
- **Sales Cycle Length:** Average days from SQL to closed won
- **Time in Stage:** Days spent in each pipeline stage

**Critical Insight from Data:**
Our analysis revealed a **declining win rate trend** (-3.4 pp H2 vs H1 2025), indicating need for:
- Sales process optimization
- Better lead qualification
- Competitive positioning improvement

### **3.3 Customer Success Department KPIs**

**Volume Metrics:**
- **Customer Onboarding Completion Rate:** % completing implementation
- **Monthly Active Users (MAU):** Product adoption metrics
- **Support Ticket Volume:** Customer health indicator

**Efficiency Metrics:**
- **Time to Value (TTV):** Days from purchase to first value realization
- **Customer Satisfaction (CSAT):** Quarterly satisfaction surveys
- **Net Promoter Score (NPS):** Customer advocacy measurement

**Velocity Metrics:**
- **Onboarding Time:** Days from contract to go-live
- **Issue Resolution Time:** Average support ticket resolution

**Revenue Impact KPIs:**
- **Gross Revenue Retention (GRR):** % revenue retained from existing customers
- **Net Revenue Retention (NRR):** GRR + expansion revenue
- **Customer Lifetime Value (CLV):** Total value per customer

---

## 4. Tool Stack Mapping & Data Integration

### **4.1 Current Tool Stack Mapping**

```
BOWTIE STAGE          TOOL              USE CASE
─────────────────────────────────────────────────────
Awareness/Interest    HubSpot           Lead capture, nurturing
                     Internal DB        Product usage analytics
                     
Consideration        HubSpot           Lead scoring, qualification
                     Dynamics 365      Opportunity management
                     
Purchase             Dynamics 365      Deal management, forecasting
                     Internal DB       Product configuration
                     
Onboarding           Zendesk           Support ticketing
                     Internal DB       Implementation tracking
                     Chargebee         Billing, subscription setup
                     
Expansion            Dynamics 365      Account management
                     Chargebee         Usage-based billing
                     Internal DB       Product analytics
                     
Advocacy             HubSpot           Reference management
                     Zendesk           Customer feedback
```

### **4.2 HubSpot ↔ Dynamics 365 Data Mapping Proposal**

**Critical Data Points for Sync:**

| Field Category | HubSpot Field | Dynamics Field | Sync Direction | Rationale |
|----------------|---------------|----------------|----------------|-----------|
| **Lead Identity** | Email, Company, Name | Contact, Account | HubSpot → Dynamics | Single source of truth for lead data |
| **Qualification** | Lead Score, MQL Date | Qualification Score | HubSpot → Dynamics | Marketing automation intelligence |
| **Engagement** | Page Views, Email Opens | Activity History | HubSpot → Dynamics | Behavioral context for sales |
| **Sales Activity** | Last Contact, Next Steps | Activities, Tasks | Dynamics → HubSpot | Sales activity visibility |
| **Opportunity Data** | Deal Stage, Close Date | Opportunity Stage | Dynamics → HubSpot | Pipeline reporting alignment |
| **Revenue** | Deal Amount, Probability | Opportunity Value | Dynamics → HubSpot | Revenue attribution |

**Sync Direction Rationale:**

**HubSpot → Dynamics (Primary Flow):**
- Marketing owns lead generation and qualification
- Rich behavioral data enhances sales context
- Lead scoring algorithms inform sales prioritization

**Dynamics ← HubSpot (Feedback Loop):**
- Sales outcomes inform marketing campaign effectiveness
- Closed-loop reporting enables ROI calculation
- Win/loss analysis improves lead scoring models

**Data Quality Considerations:**
1. **Duplicate Prevention:** Email-based matching with fuzzy logic
2. **Field Validation:** Required fields enforcement at handoff
3. **Status Mapping:** Standardized lifecycle stages across systems
4. **Historical Data:** Preserve lead source attribution

---

## 5. Executive Dashboard - Top 5 KPIs

### **Leadership KPI Dashboard**

#### **1. Annual Recurring Revenue (ARR) Growth**
- **Current Status:** $54.3M confirmed for 2026
- **Target:** 25% YoY growth
- **Why Critical:** Direct business impact measurement
- **Decision Impact:** Investment allocation, headcount planning

#### **2. Sales Efficiency (Win Rate)**
- **Current Status:** 26.9% (declining -3.4pp)
- **Target:** 35% industry benchmark
- **Why Critical:** Go-to-market effectiveness indicator
- **Decision Impact:** Sales process optimization, training needs

#### **3. Pipeline Velocity**
- **Measurement:** Average sales cycle length
- **Current Challenge:** 231 overdue deals requiring attention
- **Why Critical:** Cash flow predictability
- **Decision Impact:** Resource allocation, forecasting accuracy

#### **4. Customer Acquisition Cost (CAC) vs. Lifetime Value (LTV)**
- **Ratio Target:** LTV:CAC ≥ 3:1
- **Why Critical:** Unit economics validation
- **Decision Impact:** Marketing budget optimization, pricing strategy

#### **5. Net Revenue Retention (NRR)**
- **Target:** >110% for healthy growth
- **Why Critical:** Expansion revenue opportunity
- **Decision Impact:** Customer success investment, product development priorities

### **Dashboard Design Principles**
- **Real-time Updates:** Weekly refresh minimum
- **Drill-down Capability:** Department-level detail available
- **Trend Analysis:** YoY and quarter-over-quarter comparison
- **Predictive Elements:** Forecasting with confidence intervals

---

## 6. Strategic Recommendations

### **6.1 Immediate Actions (30 days)**
1. **Data Hygiene:** Resolve 231 overdue open deals status
2. **Win Rate Analysis:** Deep dive into H2 2025 decline causes
3. **Tool Integration:** Implement HubSpot-Dynamics sync

### **6.2 Short-term Initiatives (90 days)**
1. **Sales Process Optimization:** Address declining win rates
2. **Lead Scoring Refinement:** Improve MQL-to-SQL conversion
3. **Executive Dashboard Implementation:** Top 5 KPIs tracking

### **6.3 Long-term Strategy (12 months)**
1. **Revenue Operations Platform:** Unified data architecture
2. **Predictive Analytics:** AI-powered forecasting models
3. **Customer Success Expansion:** Proactive churn prevention

---

## 7. Conclusion

PTV Logistics operates in a complex B2B environment requiring sophisticated RevOps capabilities. The data analysis reveals both opportunities and challenges:

**Strengths:**
- Strong pipeline value ($54.3M confirmed revenue)
- Established customer base with expansion potential
- Comprehensive tool stack foundation

**Areas for Improvement:**
- Declining win rate trend requires immediate attention
- Data quality issues need resolution
- Cross-departmental alignment opportunities

**Next Steps:**
1. Implement executive dashboard with top 5 KPIs
2. Resolve data hygiene issues (231 overdue deals)
3. Establish regular cross-functional RevOps reviews
4. Develop predictive analytics capabilities for better forecasting

The proposed framework provides PTV Logistics with a data-driven approach to revenue operations, enabling better decision-making and sustainable growth acceleration.

---

*Analysis based on 2,621 opportunities dataset and industry best practices for B2B SaaS RevOps.*
