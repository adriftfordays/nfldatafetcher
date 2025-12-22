import csv
import json

def load_csv(filename):
    """Load CSV file adn return list of dictionaries"""
    servers = []
        
    with open('server_inventory.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert numeric strings to actual numbers
            row['cpu_cores'] = int(row['cpu_cores'])
            row['ram_gb'] = int(row['ram_gb'])
            servers.append(row)
        
    return servers

def filter_servers(servers, environment=None, status=None):
    """Filter Servers by environment and/or status"""
    filtered = servers
    
    if environment:
        filtered = [s for s in filtered if s['environment'] == environment]
        
    if status:
        filtered = [s for s in filtered if s['status'] == status]
        
    return filtered
    


def save_json(data, filename):
    """Save data to JSON file"""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)
    print(f"✓ Saved {len(data)} records to {filename}")
    
def generate_report(servers):
    """Generate summary report from server data"""
    
    # Count servers by environment
    env_counts = {}
    for server in servers:
        env = server['environment']
        if env in env_counts:
            env_counts[env] += 1
        else:
            env_counts[env] = 1
            
    # Count Servers
    status_counts = {}
    for server in servers:
        status = server['status']
        if status in status_counts:
            status_counts[status] += 1
        else:
            status_counts[status] = 1
            
    # Calculate total resources 
    total_cpu = sum(server['cpu_cores'] for server in servers)
    total_ram = sum(server['ram_gb'] for server in servers)
    
    #Build Report
    report = []
    report.append("=" * 50)
    report.append("SERVER INVENTORY REPORT")
    report.append(f"\nTotal Servers: {len(servers)}")
    report.append(f"Total CPU Cores: {total_cpu}")
    report.append(f"Total RAM: {total_ram} GB")
    report.append("\n--- By Environment ---")
    for env, count in env_counts.items():
        report.append(f" {env}: {count}")
    report.append("\n--- By Status ---")
    for status, count in status_counts.items():
        report.append(f" {status}: {count}")
    report.append("\n" + "=" * 50)
    
    return "\n".join(report)       

def save_report(report, filename):
    """Save report to text file"""
    with open(filename, 'w') as file:
        file.write(report)
    print(f"✓ Report saved to {filename}")
    
#Test It
servers = load_csv('server_inventory.csv')
print(f"Loaded {len(servers)} servers")
save_json(servers, 'server_inventory.json')

#Generate and print report
report = generate_report(servers)
print(report)
save_report(report, 'server_report.txt')

prod_servers = filter_servers(servers, environment='production')
prod_report = generate_report(prod_servers)
print("\n\nPRODUCTION ONLY:")
print(prod_report)