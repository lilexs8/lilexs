from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.session import Base

class Organization(Base):
    __tablename__ = "organizations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    plan = Column(String, default="free")
    status = Column(String, default="active")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"))
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    status = Column(String, default="active")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Asset(Base):
    __tablename__ = "assets"
    id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"))
    name = Column(String, nullable=False)
    asset_type = Column(String, nullable=False)
    ip_address = Column(String)
    domain = Column(String)
    criticality = Column(String, default="medium")
    risk_level = Column(String, default="medium")
    status = Column(String, default="active")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Finding(Base):
    __tablename__ = "findings"
    id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"))
    asset_id = Column(Integer, ForeignKey("assets.id"), nullable=True)
    title = Column(String, nullable=False)
    severity = Column(String, default="medium")
    category = Column(String)
    description = Column(Text, nullable=False)
    evidence = Column(Text)
    business_impact = Column(Text)
    recommendation = Column(Text)
    status = Column(String, default="open")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class AttackPath(Base):
    __tablename__ = "attack_paths"
    id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"))
    name = Column(String, nullable=False)
    risk_level = Column(String, default="high")
    path_summary = Column(Text, nullable=False)
    business_impact = Column(Text)
    lix_analysis = Column(Text)
    status = Column(String, default="active")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class ThreatMemory(Base):
    __tablename__ = "threat_memory"
    id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"))
    memory_type = Column(String, nullable=False)
    title = Column(String, nullable=False)
    summary = Column(Text, nullable=False)
    severity = Column(String, default="medium")
    trend = Column(String, default="stable")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"))
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    title = Column(String, nullable=False)
    report_type = Column(String, default="executive")
    language = Column(String, default="en")
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class LixConversation(Base):
    __tablename__ = "lix_conversations"
    id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    title = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class LixMessage(Base):
    __tablename__ = "lix_messages"
    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("lix_conversations.id"))
    role = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    context_type = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
