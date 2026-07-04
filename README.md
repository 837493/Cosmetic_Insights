# 💄 Cosmetic Insights: Navigating Cosmetics Trends and Consumer Insights

An interactive Tableau dashboard analyzing cosmetics sales data to uncover trends in revenue, brand performance, regional demand, customer demographics, and product ratings.

---

## 📌 Project Objective

The goal of this project is to explore cosmetics and skincare sales data to answer key business questions:
- Which product categories and brands generate the most revenue?
- How does revenue trend over time?
- Which countries/regions drive the most sales?
- How are products rated across categories?
- What do customer demographics (age, gender, skin type) reveal about buying patterns?

---

## 🗂️ Dataset

- **File:** `cosmetics_insights_dataset.csv`
- **Rows:** 2,000 transaction records
- **Fields:** Order ID, Date, Brand, Category, Subcategory, Price (USD), Discount (%), Units Sold, Revenue (USD), Rating, Number of Reviews, Region, Country, Sales Channel, Customer Gender, Customer Age Group, Customer Skin Type

---

## 🛠️ Tools & Methodology

1. **Data Preparation:** Cleaned and structured cosmetics sales data in CSV format.
2. **Visualization:** Built 5 worksheets in **Tableau Public**:
   - Revenue by Category
   - Revenue Trend (monthly)
   - Top Brands by Revenue
   - Revenue by Country
   - Average Rating by Category
3. **Dashboard Assembly:** Combined all worksheets into a single interactive dashboard with cross-filtering — clicking any category updates all other charts.

---

## 📊 Key Insights

- **Top Category:** Makeup and Skincare lead in total revenue among all categories.
- **Revenue Trend:** Monthly revenue shows fluctuation across 2023–2024, with visible peaks and dips rather than flat/stable demand.
- **Top Brands:** L'Oréal and Maybelline are the highest revenue-generating brands in the dataset.
- **Regional Performance:** UAE and UK show the strongest revenue contribution among the countries analyzed.
- **Ratings:** Average product ratings stay fairly consistent (around 4.0) across all categories, suggesting stable customer satisfaction regardless of product type.

*(Update these bullet points with your own exact numbers/findings once you review your final charts.)*

---

## 🖼️ Dashboard Preview

> Add a screenshot of your final Tableau dashboard here:
```markdown
![Dashboard Screenshot](dashboard_screenshot.png)
```

---

## 📁 Repository Structure

```
cosmetic-insights-tableau/
│
├── README.md                          # Project write-up (this file)
├── cosmetics_insights_dataset.csv     # Source dataset
├── Cosmetic_Insights.twbx             # Tableau packaged workbook
└── dashboard_screenshot.png           # Screenshot of the final dashboard
```

---

## 🚀 How to Upload This Project to GitHub

### Step 1: Create a GitHub repository
1. Go to [github.com](https://github.com) and log in.
2. Click the **+** icon (top-right) → **New repository**.
3. Name it something like `cosmetic-insights-tableau`.
4. Set it to **Public** (so it's visible to reviewers).
5. Click **Create repository**.

### Step 2: Prepare your files
Gather these files into one folder on your computer:
- This `README.md`
- Your dataset: `cosmetics_insights_dataset.csv`
- Your Tableau file: save your workbook as a **packaged workbook** so it includes the data —
  - In Tableau: **File > Save As** → choose file type **Tableau Packaged Workbook (.twbx)**
- A screenshot of your finished dashboard (Windows: `Win + Shift + S` to snip, save as `dashboard_screenshot.png`)

### Step 3: Upload via GitHub website (easiest, no coding needed)
1. Open your new repository page.
2. Click **Add file > Upload files**.
3. Drag and drop all your files (README.md, .csv, .twbx, .png) into the upload box.
4. Scroll down, add a commit message like "Initial upload of Cosmetic Insights project."
5. Click **Commit changes**.

Your project is now live on GitHub! 🎉

### Optional: Publish to Tableau Public for a live interactive link
1. In Tableau, go to **File > Save to Tableau Public**.
2. Sign in/create a free Tableau Public account.
3. Once uploaded, copy the shareable link.
4. Add it to your README under a new section, e.g.:
   ```markdown
   ## 🔗 Live Interactive Dashboard
   [View on Tableau Public](your-link-here)
   ```

---

## ✅ Conclusion

This project demonstrates how Tableau can transform raw cosmetics sales data into actionable business insights — identifying top-performing categories, brands, and regions, while surfacing customer rating and demand patterns that can guide marketing and inventory decisions.
